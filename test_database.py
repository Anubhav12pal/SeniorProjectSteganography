import os
import tkinter as tk
from tkinter import filedialog
from Database import Database

# Initialize the database connection
user = os.getenv("DB2_USER")
password = os.getenv("DB2_PASSWORD")
host = os.getenv("DB2_HOST", "localhost")
dbname = os.getenv("DB2_NAME")

db = Database(user=user, password=password, host=host, dbname=dbname)

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    print("Opening file dialog...")
    file_path = filedialog.askopenfilename()
    root.destroy()  # Destroy the root window after file dialog is closed
    print(f"File selected: {file_path}")
    return file_path

def save_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
    root.destroy()  # Destroy the root window after file dialog is closed
    return save_path

def main():
    while True:
        print("Select an option:")
        print("10: Add user")
        print("20: Login")
        print("30: Add image")
        print("40: Retrieve image")
        print("50: Exit")

        option = int(input("Enter option: "))

        if option == 10:
            username = input("Enter username: ")
            password = input("Enter password: ")
            db.saveCredentials(username, password)
        elif option == 20:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if db.validatePassword(username, password):
                print("Login successful.")
            else:
                print("Invalid username or password.")
        elif option == 30:
            username = input("Enter username: ")
            image_name = input("Enter image name: ")
            image_path = select_file()
            if not os.path.exists(image_path):
                print(f"Image file not found: {image_path}")
                continue
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
            db.saveImage(username, image_name, image_data)
            print("Image saved successfully.")
        elif option == 40:
            username = input("Enter username: ")
            image_name = input("Enter image name: ")
            image_data = db.retrieveImage(username, image_name)
            if image_data:
                save_path = save_file_dialog()
                if save_path:
                    with open(save_path, "wb") as image_file:
                        image_file.write(image_data)
                    print(f"Image retrieved and saved to {save_path}.")
                else:
                    print("Save operation cancelled.")
            else:
                print("No image found with the given name for the specified user.")
        elif option == 50:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()