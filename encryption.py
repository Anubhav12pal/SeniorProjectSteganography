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
    input_image = "C:/Users/Dishant Borda/Desktop/Rainier.bmp"
    output_image = "/Users/Dishant Borda/Desktop/rain.bmp"
    message = "Digital Steganography involves embedding hidden information within digital media files. Our project aims to create a user-friendly tool using Python and React.js to allow secure data hiding and extraction. This tool will support multiple file formats, incorporate encryption, and provide a seamless experience for end-users."
    
    Steganography.encrypt_message(input_image, output_image, message)
    
    encoded_image = "/Users/Dishant Borda/Desktop/rain.bmp"
    Steganography.decrypt_message(encoded_image)

if __name__ == "__main__":
    main()