from encryption import Steganography
import matplotlib.pyplot as plt

class SteganographyProcessor:
    def __init__(self):
        self.input_image = 'images/inputImage.png'
        self.encoded_images_path = 'images/EncodedImages/'
        self.encoded_images_path2 = 'images/EncodedImages2/'
    
    

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
    
    def store_mse_for_path(self, path):
        mse_values = []
        for i in range(1, 11):
            output_image = f'{path}encodedImage{i}.png'
            mse = Steganography.calculate_mse(self.input_image, output_image)
            mse_values.append(mse)
        return mse_values

    def store_psnr_for_path(self, path):
        psnr_values = []
        for i in range(1, 11):
            output_image = f'{path}encodedImage{i}.png'
            psnr = Steganography.calculate_psnr(self.input_image, output_image)
            psnr_values.append(psnr)
        return psnr_values
    
    def create_encoded2(self):
        for i in range(1, 11):
            message_file = f'f{i}.txt'
            output_image = f'{self.encoded_images_path2}encodedImage{i}.png'
            
            with open(message_file, 'r') as file:
                message = file.read()
            
            Steganography.encrypt_message_2(self.input_image, output_image, message)
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

    # def store_mse(self):
    #     mse_values = []
    #     for i in range(1, 11):
    #         output_image = f'{self.encoded_images_path}encodedImage{i}.png'
    #         mse = Steganography.calculate_mse(self.input_image, output_image)
    #         mse_values.append(mse)
    #     return mse_values

    # def store_psnr(self):
    #     psnr_values = []
    #     for i in range(1, 11):
    #         output_image = f'{self.encoded_images_path}encodedImage{i}.png'
    #         psnr = Steganography.calculate_psnr(self.input_image, output_image)
    #         psnr_values.append(psnr)
    #     return psnr_values

def main():
    processor = SteganographyProcessor()
    # process.create_encoded()
    # processor.create_encoded2()
    mses = processor.store_mse_for_path("images/EncodedImages/")
    psnrs = processor.store_psnr_for_path("images/EncodedImages/")

    mses2 = processor.store_mse_for_path("images/EncodedImages2/")
    psnrs2 = processor.store_psnr_for_path("images/EncodedImages2/")
    size = processor.countChars()

    print(mses)
    print(psnrs)

    print(mses2)
    print(psnrs2)
   
    print(size)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(size, mses, marker='o', label='EncodedImages')
    plt.plot(size, mses2, marker='x', label='EncodedImages2')
    plt.title('MSE vs Message Size')
    plt.xlabel('Message Size (characters)')
    plt.ylabel('MSE')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(size, psnrs, marker='o', label='EncodedImages')
    plt.plot(size, psnrs2, marker='x', label='EncodedImages2')
    plt.title('PSNR vs Message Size')
    plt.xlabel('Message Size (characters)')
    plt.ylabel('PSNR')
    plt.legend()

    plt.tight_layout()
    plt.show()
    

if __name__ == "__main__":
    main()
    

    

    

    

    