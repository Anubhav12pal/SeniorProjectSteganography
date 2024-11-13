from encryption import Steganography

# Path to the encoded image
encoded_image_path = "/Users/o_msb8/Desktop/School/University/Senior_Project/SeniorProjectSteganography/encoded_images/encoded_image1.png"

try:
    # Decode the message
    decoded_message = Steganography.decrypt_message(encoded_image_path)
    if decoded_message:
        print(f"Decoded message: {repr(decoded_message)}")
    else:
        print("No hidden message was found.")
except Exception as e:
    print(f"Error while decoding: {e}")
