from stegano import lsb
from PIL import Image

class Steganography:
    @staticmethod
    def convert_png_to_bmp(png_image_path, bmp_image_path):
        # Convert PNG image to BMP
        img = Image.open(png_image_path)
        img.save(bmp_image_path, format = "BMP")
        print(f"Converted PNG to BMP: {bmp_image_path}")

    @staticmethod
    def encrypt_message(input_image_path, output_image_path, secret_message):
        encoded_image = lsb.hide(input_image_path, secret_message)
        encoded_image.save(output_image_path,format = "BMP")
        print(f"Message hidden and saved in {output_image_path}")

    @staticmethod
    def decrypt_message(encoded_image_path):
        secret_message = lsb.reveal(encoded_image_path)
        if secret_message:
            print(f"Hidden message: {secret_message}")
        else:
            print("No hidden message found!")

def main():
    png_image = "C:/Users/alvin/Downloads/SeniorProjectSteganography-main/SeniorProjectSteganography-main/digital_steganography/public/Images/Logo.png"
    bmp_image = "C:/Users/alvin/Downloads/SeniorProjectSteganography-main/SeniorProjectSteganography-main/digital_steganography/public/Images/Logo.bmp"
    output_bmp_image = "C:/Users/alvin/Downloads/SeniorProjectSteganography-main/SeniorProjectSteganography-main/digital_steganography/public/Images/Logo_with_message.bmp"
    message = "Secret Message"
    
    # Convert PNG to BMP
    Steganography.convert_png_to_bmp(png_image, bmp_image)

    #Encrypt a secret message into the BMP image
    Steganography.encrypt_message(bmp_image, output_bmp_image, message)
    
    #Extract the hiddgen message from the BMp image
    Steganography.decrypt_message(output_bmp_image)

if __name__ == "__main__":
    main()