from stegano import lsb
import numpy as np
from PIL import Image
import math

class Steganography:
    @staticmethod
    def encrypt_message(input_image_path, output_image_path, secret_message):
        encoded_image = lsb.hide(input_image_path, secret_message)
        encoded_image.save(output_image_path)
        print(f"Message hidden and saved in {output_image_path}")

    @staticmethod
    def decrypt_message(encoded_image_path):
        secret_message = lsb.reveal(encoded_image_path)
        if secret_message:
            print(f"Hidden message: {secret_message}")
        else:
            print("No hidden message found!")

    @staticmethod
    def calculate_mse(image_path1, image_path2):
        image1 = np.array(Image.open(image_path1))
        image2 = np.array(Image.open(image_path2))
        mse = np.mean((image1 - image2) ** 2)
        return mse

    @staticmethod
    def calculate_psnr(image_path1, image_path2):
        mse = Steganography.calculate_mse(image_path1, image_path2)
        if mse == 0:
            return float('inf')
        max_pixel = 255.0
        psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
        return psnr

def main():
    input_image = "C:/Users/gpand/Downloads/image metadata/Rainier.bmp"
    output_image = "C:/Users/gpand/Downloads/image metadata/encoded_image.png"
    message = "H" * 500000
    
    # Encrypt the message into the image
    Steganography.encrypt_message(input_image, output_image, message)
    
    # Decrypt the message from the encoded image
    encoded_image = "C:/Users/gpand/Downloads/image metadata/encoded_image.png"
    Steganography.decrypt_message(encoded_image)
    
    # Calculate MSE and PSNR between the original and encoded images
    mse_original = Steganography.calculate_mse(input_image, input_image)
    psnr_original = Steganography.calculate_psnr(input_image, input_image)
    
    mse_encoded = Steganography.calculate_mse(input_image, encoded_image)
    psnr_encoded = Steganography.calculate_psnr(input_image, encoded_image)
    
    print(f"MSE of original image: {mse_original}")
    print(f"PSNR of original image: {psnr_original}")
    print(f"MSE between original and encoded image: {mse_encoded}")
    print(f"PSNR between original and encoded image: {psnr_encoded}")

if __name__ == "__main__":
    main()