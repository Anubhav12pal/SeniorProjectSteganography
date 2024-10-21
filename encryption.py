from stegano import lsb
import numpy as np
from PIL import Image


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

def main():
    # input_image = "images/inputImage.png"
    # output_image = "images/output.png"
    # message = "Hello this is Penaldo"
    
    # Steganography.encrypt_message(input_image, output_image, message)
    
    # encoded_image = "images/output.png"
    # Steganography.decrypt_message(encoded_image)
    ans = Steganography.calculate_mse("images/inputImage.png", "images/output.png")
    print(ans)

if __name__ == "__main__":
    main()