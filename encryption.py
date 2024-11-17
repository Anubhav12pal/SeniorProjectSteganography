from stegano import lsb
import numpy as np
from PIL import Image
import math

class Steganography:
    @staticmethod
    def encrypt_message_2(input_image_path, output_image_path, secret_message):
        image = Image.open(input_image_path)
        image = image.convert('RGB')
        pixels = np.array(image)

        # Convert the message to binary
        binary_message = ''.join([format(ord(char), '08b') for char in secret_message])
        binary_message += '1111111111111110'  # Delimiter to mark the end of the message

        data_index = 0
        message_length = len(binary_message)

        for row in pixels:
            for pixel in row:
                for color in range(3):  # Iterate over R, G, B channels
                    if data_index < message_length:
                        # Modify the last 2 bits of the pixel
                        pixel[color] = (pixel[color] & ~3) | int(binary_message[data_index:data_index+2], 2)
                        data_index += 2

        encoded_image = Image.fromarray(pixels)
        encoded_image.save(output_image_path)
        print(f"Message hidden and saved in {output_image_path}")

    @staticmethod
    def decrypt_message_2(encoded_image_path):
        image = Image.open(encoded_image_path)
        image = image.convert('RGB')
        pixels = np.array(image)

        binary_message = ''
        for row in pixels:
            for pixel in row:
                for color in range(3):  # Iterate over R, G, B channels
                    binary_message += format(pixel[color] & 3, '02b')

        # Split the binary message into 8-bit chunks and convert to characters
        message = ''
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            if byte == '11111110':  # Delimiter to mark the end of the message
                break
            message += chr(int(byte, 2))

        if message:
            print(f"Hidden message: {message}")
        else:
            print("No hidden message found!")

    @staticmethod
    def encrypt_message(input_image_path, output_image_path, secret_message):
        encoded_image = lsb.hide(input_image_path, secret_message)

        # Convert RGBA to RGB if saving as JPEG
        if output_image_path.lower().endswith(('.jpg', '.jpeg')) and encoded_image.mode == 'RGBA':
            encoded_image = encoded_image.convert('RGB')

        encoded_image.save(output_image_path)
        print(f"Message hidden and saved in {output_image_path}")

    @staticmethod
    def decrypt_message(encoded_image_path):
        secret_message = lsb.reveal(encoded_image_path)
        if secret_message:
            print(f"Hidden message: {secret_message}")
            return secret_message.strip()  # Remove leading/trailing whitespace if any
        else:
            print("No hidden message found!")
            return None

    @staticmethod
    def calculate_mse(image_path1, image_path2):
        image1 = Image.open(image_path1).convert('RGB')
        image2 = Image.open(image_path2).convert('RGB')
        image1 = np.array(image1)
        image2 = np.array(image2)
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

    @staticmethod
    def calculate_max_message_size(image_path):
        image = Image.open(image_path)
        width, height = image.size
        # Assuming 3 color channels (RGB) and 2 bits per channel
        max_message_size = (width * height * 3 * 2) // 8  # in bytes
        return max_message_size - 10  # Reduce the size slightly to ensure it fits within the allowable limits

def main():
    input_image = "C:/Users/gpand/Downloads/image metadata/Rainier.bmp"
    output_image = "C:/Users/gpand/Downloads/image metadata/encoded_image.png"
    max_size = Steganography.calculate_max_message_size(input_image)
    print(f"Maximum message size for the image is: {max_size} bytes")

    # Reduce the message size slightly to ensure it fits within the allowable limits
    message = "H" * (max_size - 10)  # Example message length that fits within max_size

    if len(message) > max_size:
        raise ValueError(f"The message you want to hide is too long: {len(message)}. Maximum allowed size is {max_size} bytes.")

    # Encrypt the message into the image
    Steganography.encrypt_message(input_image, output_image, message)

    # Decrypt the message from the encoded image
    encoded_image = "C:/Users/gpand/Downloads/image metadata/encoded_image.png"
    Steganography.decrypt_message(encoded_image)

    # Calculate MSE and PSNR between the original and encoded images
    mse_encoded = Steganography.calculate_mse(input_image, encoded_image)
    psnr_encoded = Steganography.calculate_psnr(input_image, encoded_image)

    print(f"MSE between original and encoded image: {mse_encoded}")
    print(f"PSNR between original and encoded image: {psnr_encoded}")

if __name__ == "__main__":
    main()
