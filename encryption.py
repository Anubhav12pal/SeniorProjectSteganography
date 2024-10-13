from stegano import lsb

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

def main():
    input_image = "Image path"
    output_image = "oytput image path"
    message = "Message"
    
    Steganography.encrypt_message(input_image, output_image, message)
    
    encoded_image = "/Users/anubhav/Documents/DSA Practice with Python Take u forward/Steganography/Images/encoded.png"
    Steganography.decrypt_message(encoded_image)

if __name__ == "__main__":
    main()