import os
import tkinter as tk
from tkinter import filedialog
from stegano import lsb
import numpy as np
from PIL import Image
import math
import csv
from encryption import Steganography  # Import the Steganography class

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    print("Opening directory dialog...")
    directory_path = filedialog.askdirectory()
    root.destroy()  # Destroy the root window after directory dialog is closed
    if not directory_path:
        print("Directory selection canceled.")
        return None
    print(f"Directory selected: {directory_path}")
    return directory_path

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    print("Opening file dialog...")
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff"),
            ("All files", "*.*")
        ]
    )
    root.destroy()  # Destroy the root window after file dialog is closed
    if not file_path:
        print("File selection canceled.")
        return None
    print(f"File selected: {file_path}")
    return file_path

def save_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    save_path = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[
            ("JPEG files", "*.jpg *.jpeg"),
            ("PNG files", "*.png"),
            ("BMP files", "*.bmp"),
            ("GIF files", "*.gif"),
            ("TIFF files", "*.tiff"),
            ("All files", "*.*")
        ]
    )
    root.destroy()  # Destroy the root window after file dialog is closed
    if not save_path:
        print("Save file dialog canceled.")
        return None
    return save_path

def select_text_file():
    """Selects a text file to embed."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    print("Opening text file dialog...")
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    root.destroy()  # Destroy the root window after file dialog is closed
    if not file_path:
        print("Text file selection canceled.")
        return None
    print(f"Text file selected: {file_path}")
    return file_path

def calculate_step_size(max_size):
    num_digits = len(str(max_size))
    step_size = (10 ** (num_digits - 1))
    return step_size

def test_image(input_image, output_image, text_file):
    """Tests image encoding with a text file."""
    results = []
    
    # Read the contents of the text file with utf-8 encoding
    with open(text_file, 'r', encoding='utf-8') as file:
        message = file.read()

    # Encrypt the message from the text file into the image
    Steganography.encrypt_message(input_image, output_image, message)
    
    # Calculate MSE and PSNR between the original and encoded images
    mse_encoded = Steganography.calculate_mse(input_image, output_image)
    psnr_encoded = Steganography.calculate_psnr(input_image, output_image)
    
    # Append the results to the list
    results.append([os.path.basename(input_image), len(message), mse_encoded, psnr_encoded, os.path.basename(output_image)])
    print(f"Tested with message size: {len(message)} bytes, MSE: {mse_encoded}, PSNR: {psnr_encoded}")
    
    return results


def output_all_types(input_image, base_output_path, text_file):
    """Outputs images in all types for embedding text file content."""
    results = []
    output_formats = [".jpg", ".png", ".bmp", ".gif", ".tiff"]
    
    for fmt in output_formats:
        output_image = base_output_path + fmt
        results.extend(test_image(input_image, output_image, text_file))
    
    return results

def choose_image():
    input_image = select_file()  # Choose the input image
    if not input_image:
        return  # Exit if file selection is canceled

    text_file = select_text_file()  # Choose the text file to embed
    if not text_file:
        return  # Exit if text file selection is canceled
    
    choice = input("Enter 30 to output all types or 40 to select file output: ")
    
    if choice == "30":
        base_output_path = os.path.splitext(input_image)[0] + "_encoded"
        results = output_all_types(input_image, base_output_path, text_file)
    elif choice == "40":
        output_image = save_file_dialog()  # Choose the output image path
        if not output_image:
            return  # Exit if save file dialog is canceled
        results = test_image(input_image, output_image, text_file)
    else:
        print("Invalid choice. Please enter 30 or 40.")
        return
    
    # Generate CSV file with the results
    generate_csv(results, "results1.csv")

def bulk_image_directory():
    directory = select_directory()  # Choose the input directory
    if not directory:
        return  # Exit if directory selection is canceled
    
    text_file = select_text_file()  # Choose the text file to embed
    if not text_file:
        return  # Exit if text file selection is canceled
    
    choice = input("Enter 30 to output all types or 40 to select file output: ")
    
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
                input_image = os.path.join(root, file)
                print(f"Processing file: {input_image}")
                
                if choice == "30":
                    base_output_path = os.path.splitext(input_image)[0] + "_encoded"
                    results.extend(output_all_types(input_image, base_output_path, text_file))
                elif choice == "40":
                    output_image = save_file_dialog()  # Choose the output image path
                    if not output_image:
                        return  # Exit if save file dialog is canceled
                    results.extend(test_image(input_image, output_image, text_file))
                else:
                    print("Invalid choice. Please enter 30 or 40.")
                    return
    
    # Generate CSV file with the results
    generate_csv(results, "results1.csv")

def generate_csv(results, csv_file="results1.csv"):
    # Specify the directory where you want to save the CSV file
    directory = os.path.dirname(csv_file)
    if not directory:
        directory = os.getcwd()  # Use the current working directory if no directory is specified
    
    csv_file_path = os.path.join(directory, os.path.basename(csv_file))
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Filename", "Message Size", "MSE", "PSNR", "Output Filename"])
        writer.writerows(results)
    print(f"Results saved to {os.path.abspath(csv_file_path)}")

def generate_report(directory):
    results = []
    output_formats = [".jpg", ".png", ".bmp", ".gif", ".tiff"]
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
                input_image = os.path.join(root, file)
                for fmt in output_formats:
                    encoded_image = os.path.splitext(input_image)[0] + "_encoded" + fmt
                    if os.path.exists(encoded_image):
                        mse_encoded = Steganography.calculate_mse(input_image, encoded_image)
                        psnr_encoded = Steganography.calculate_psnr(input_image, encoded_image)
                        results.append([os.path.basename(input_image), len(encoded_image), mse_encoded, psnr_encoded, os.path.basename(encoded_image)])
    
    # Generate CSV file with the results
    generate_csv(results, "report.csv")

def test_multiple_text_files(input_image, output_image_base, text_files_dir):
    results = []
    output_formats = [".jpg", ".png", ".bmp", ".gif", ".tiff"]

    # Loop through each text file in the directory
    for text_file_name in sorted(os.listdir(text_files_dir)):
        if text_file_name.endswith(".txt"):
            text_file_path = os.path.join(text_files_dir, text_file_name)
            print(f"Processing text file: {text_file_path}")

            # Test encoding each text file into the image
            for fmt in output_formats:
                output_image = output_image_base + f"_{text_file_name.split('.')[0]}" + fmt
                results.extend(test_image(input_image, output_image, text_file_path))

    # Generate a CSV file with all results
    generate_csv(results, "results_multiple_text_files.csv")

def main():
    choice = input("Enter 10 to test a single image, 15 to generate a report, 20 to test a directory of images, or 25 to test multiple text files with a single image: ")

    if choice == "10":
        choose_image()
    elif choice == "15":
        directory = select_directory()
        if directory:
            generate_report(directory)
    elif choice == "20":
        bulk_image_directory()
    elif choice == "25":
        input_image = select_file()  # Choose the input image
        if not input_image:
            return  # Exit if file selection is canceled

        text_files_dir = select_directory()  # Select the directory with text files
        if not text_files_dir:
            return  # Exit if directory selection is canceled

        base_output_path = os.path.splitext(input_image)[0] + "_encoded"
        test_multiple_text_files(input_image, base_output_path, text_files_dir)
    else:
        print("Invalid choice. Please enter 10, 15, 20, or 25.")

if __name__ == "__main__":
    main()

