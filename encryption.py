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
    def calculate_mse(original_image_path, stego_image_path):
        original_image = np.array(Image.open(original_image_path))
        stego_image = np.array(Image.open(stego_image_path))
        mse = np.mean((original_image - stego_image) ** 2)
        return mse

    @staticmethod
    def calculate_psnr(original_image_path, stego_image_path):
        mse = Steganography.calculate_mse(original_image_path, stego_image_path)
        if mse == 0:
            return float('inf')
        max_pixel = 255.0
        psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
        return psnr

def main():
    input_image = "input_filepath.jpg"
    output_image = "output_filepath.png"
    message = "Hello this is Penaldo"
    
    Steganography.encrypt_message(input_image, output_image, message)
    
    encoded_image = "encoded_image_filepath.png"
    Steganography.decrypt_message(encoded_image)
    
    mse = Steganography.calculate_mse(input_image, encoded_image)
    print(f"MSE: {mse}")
    
    psnr = Steganography.calculate_psnr(input_image, encoded_image)
    print(f"PSNR: {psnr}")

if __name__ == "__main__":
    main()