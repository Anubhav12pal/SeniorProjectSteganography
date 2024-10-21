from stegano import lsb
import time

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

# Stress test for large messages
def stress_test_large_message(input_image, output_image):
    large_message = "A" * 100000  # A message of 100,000 characters
    print("Starting large message stress test...")
    
    try:
        Steganography.encrypt_message(input_image, output_image, large_message)
        Steganography.decrypt_message(output_image)
        print("Large message stress test passed!")
    except Exception as e:
        print(f"Large message stress test failed: {e}")

# Stress test for large images
def stress_test_large_image(input_image, output_image, message):
    print("Starting large image stress test...")
    
    try:
        Steganography.encrypt_message(input_image, output_image, message)
        Steganography.decrypt_message(output_image)
        print("Large image stress test passed!")
    except Exception as e:
        print(f"Large image stress test failed: {e}")

# Stress test for unsupported formats
def stress_test_unsupported_format(input_image, output_image, message):
    print("Starting unsupported format stress test...")
    
    try:
        Steganography.encrypt_message(input_image, output_image, message)
        print("Unsupported format stress test passed!")
    except Exception as e:
        print(f"Unsupported format stress test failed: {e}")

# Stress test for corrupted images
def stress_test_corrupted_image(input_image):
    print("Starting corrupted image stress test...")
    
    try:
        Steganography.decrypt_message(input_image)
        print("Corrupted image stress test passed!")
    except Exception as e:
        print(f"Corrupted image stress test failed: {e}")

# High-frequency stress test
def stress_test_high_frequency(input_image, output_image, message, iterations=1000):
    start_time = time.time()
    print(f"Starting high-frequency stress test with {iterations} iterations...")
    
    try:
        for i in range(iterations):
            Steganography.encrypt_message(input_image, output_image, message)
            Steganography.decrypt_message(output_image)
            if (i + 1) % 100 == 0:
                print(f"Iteration {i + 1}/{iterations} completed")
        print("High-frequency stress test passed!")
    except Exception as e:
        print(f"High-frequency stress test failed: {e}")
    
    end_time = time.time()
    print(f"Stress test completed in {end_time - start_time:.2f} seconds.")

# Stress test for edge cases (zero-length message, short message)
def stress_test_edge_cases(input_image, output_image):
    print("Starting edge case stress tests...")
    
    # Test zero-length message
    try:
        Steganography.encrypt_message(input_image, output_image, "")
        Steganography.decrypt_message(output_image)
        print("Zero-length message stress test passed!")
    except Exception as e:
        print(f"Zero-length message stress test failed: {e}")
    
    # Test extremely short message
    try:
        Steganography.encrypt_message(input_image, output_image, "A")
        Steganography.decrypt_message(output_image)
        print("Short message stress test passed!")
    except Exception as e:
        print(f"Short message stress test failed: {e}")

# Stress test for invalid inputs (non-existent image, non-image file)
def stress_test_invalid_input():
    print("Starting invalid input stress tests...")
    
    try:
        Steganography.encrypt_message("C:\\Users\\Dishant Borda\\Desktop\\non_existent_image.bmp", "C:\\Users\\Dishant Borda\\Desktop\\output.bmp", "Test message")
        print("Non-existent file test passed!")
    except Exception as e:
        print(f"Non-existent file test failed: {e}")
    
    try:
        Steganography.encrypt_message("C:\\Users\\Dishant Borda\\Desktop\\text_file.txt", "C:\\Users\\Dishant Borda\\Desktop\\output.bmp", "Test message")
        print("Non-image file test passed!")
    except Exception as e:
        print(f"Non-image file test failed: {e}")

# Main function to run all stress tests
def run_stress_tests():
    input_image = "C:\\Users\\Dishant Borda\\Desktop\\Rainier.bmp" # Replace with a valid input image path
    output_image = "C:\\Users\\Dishant Borda\\Desktop\\rain.bmp" # Replace with a valid output image path
    large_image = "C:\\Users\\Dishant Borda\\Desktop\\large_image.jpg"  # Replace with a valid large image path
    corrupted_image = "C:\\Users\\Dishant Borda\\Desktop\\corrupted_image.bmp"  # Replace with a corrupted image path
    unsupported_image = "C:\\Users\\Dishant Borda\\Downloads\\images.png" # Replace with an unsupported image format
    message = "Digital Steganography involves embedding hidden information within digital media files. Our project aims to create a user-friendly tool using Python and React.js to allow secure data hiding and extraction. This tool will support multiple file formats, incorporate encryption, and provide a seamless experience for end-users."

    # Run each stress test
    stress_test_high_frequency(input_image, output_image, message)
    stress_test_large_message(input_image, output_image)
    stress_test_large_image(large_image, output_image, message)
    stress_test_unsupported_format(unsupported_image, output_image, message)
    stress_test_corrupted_image(corrupted_image)
    stress_test_edge_cases(input_image, output_image)
    stress_test_invalid_input()

if __name__ == "__main__":
    run_stress_tests()
