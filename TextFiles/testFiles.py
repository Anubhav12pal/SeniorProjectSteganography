from encryption import Steganography
import matplotlib.pyplot as plt

class SteganographyProcessor:
    def __init__(self):
        self.input_image = 'images/inputImage.png'
        self.encoded_images_path = 'images/EncodedImages/'
    
    

    def plot_metrics(self, sizes, mses, psnrs):
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.plot(sizes, mses, marker='o')
        plt.title('MSE vs Message Size')
        plt.xlabel('Message Size (characters)')
        plt.ylabel('MSE')

        plt.subplot(1, 2, 2)
        plt.plot(sizes, psnrs, marker='o')
        plt.title('PSNR vs Message Size')
        plt.xlabel('Message Size (characters)')
        plt.ylabel('PSNR')

        plt.tight_layout()
        plt.show()

    def countChars(self):
        char_counts = []
        for i in range(1, 11):
            message_file = f'f{i}.txt'
            with open(message_file, 'r') as file:
                message = file.read()
            char_counts.append(len(message))
        return char_counts
    
    
    def create_encoded(self):
        for i in range(1, 11):
            message_file = f'f{i}.txt'
            output_image = f'{self.encoded_images_path}encodedImage{i}.png'
            
            with open(message_file, 'r') as file:
                message = file.read()
            
            Steganography.encrypt_message(self.input_image, output_image, message)

    def decode(self):
        message = Steganography.decrypt_message(f'{self.encoded_images_path}encodedImage10.png')
        print(message)

    def store_mse(self):
        mse_values = []
        for i in range(1, 11):
            output_image = f'{self.encoded_images_path}encodedImage{i}.png'
            mse = Steganography.calculate_mse(self.input_image, output_image)
            mse_values.append(mse)
        return mse_values

    def store_psnr(self):
        psnr_values = []
        for i in range(1, 11):
            output_image = f'{self.encoded_images_path}encodedImage{i}.png'
            psnr = Steganography.calculate_psnr(self.input_image, output_image)
            psnr_values.append(psnr)
        return psnr_values

def main():
    processor = SteganographyProcessor()
    # processor.create_encoded()
    mses = processor.store_mse()
    psnrs = processor.store_psnr()
    size = processor.countChars()

    print(mses)
    print(psnrs)
    print(size)

    processor.plot_metrics(size, mses, psnrs)
    

if __name__ == "__main__":
    main()
    

    

    

    

    