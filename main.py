import cv2
import numpy as np
import os  # For handling file paths

class ImageCompression:
    def __init__(self, image_path, k):
        self.image_path = image_path
        self.k = k
        self.image = None
        self.channels = []  # Store image channels as a list
        self.U = [None] * 3
        self.S = [None] * 3
        self.Vt = [None] * 3
        self.S_k = [None] * 3
        self.compressed_image = None
    
    def image_read(self):
        self.image = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
        if self.image is None:
            print("❌ Image data is not available")
            return None
        print("\n🔹 Original Image Shape:", self.image.shape)
        return self.image
    
    def image_split_into_rgb_channel(self):
        self.channels = list(cv2.split(self.image))  # Convert tuple to list
        print("\n🔹 Image split into RGB channels:")
        for i, channel in enumerate(["Blue", "Green", "Red"]):
            print(f"\n📌 {channel} Channel Matrix Shape: {self.channels[i].shape}")
            print(f"{channel} Channel Matrix Before Compression:\n", self.channels[i])  # Print original matrix
    
    def compute_svd(self):
        print("\n🔹 Computing SVD for each channel...")
        for i in range(3):
            U, S, Vt = np.linalg.svd(self.channels[i].astype(np.float32), full_matrices=False)
            self.U[i], self.S[i], self.Vt[i] = U, S, Vt
            print(f"\n🟢 SVD of {['Blue', 'Green', 'Red'][i]} Channel:")
            print(f"U Shape: {U.shape}, S Shape: {S.shape}, Vt Shape: {Vt.shape}")
    
    def compress_image(self):
        rows, cols = self.image.shape[:2]
        max_k = min(rows, cols)
        
        if self.k < 1 or self.k > max_k:
            print(f"❌ Invalid k. k should be between 1 and {max_k}")
            return
        
        print(f"\n🔹 Compressing image using k = {self.k} singular values...")
        for i in range(3):
            self.U[i] = self.U[i][:, :self.k]
            self.S_k[i] = np.diag(self.S[i][:self.k])
            self.Vt[i] = self.Vt[i][:self.k, :]
    
    def reconstruct_channel_rgb_after_reducing_svd(self):
        print("\n🔹 Reconstructing RGB channels using reduced SVD...")
        for i in range(3):
            self.channels[i] = np.dot(self.U[i], np.dot(self.S_k[i], self.Vt[i]))
            self.channels[i] = np.clip(self.channels[i], 0, 255).astype(np.uint8)
            print(f"\n✅ Reconstructed {['Blue', 'Green', 'Red'][i]} Channel:")
            print(f"Reconstructed Shape: {self.channels[i].shape}")
            print(f"{['Blue', 'Green', 'Red'][i]} Channel Matrix After Compression:\n", self.channels[i])  # Print reconstructed matrix
    
    def merge_channel(self):
        self.compressed_image = cv2.merge(self.channels)
        print("\n🔹 Merging RGB channels into the final compressed image.")

    def display_image(self):
        cv2.imshow("Compressed Image", self.compressed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def save_compressed_image(self, output_path):
        if os.path.isdir(output_path):  # If user gives a directory, add a filename
            output_path = os.path.join(output_path, "compressed_image.jpg")
        
        success = cv2.imwrite(output_path, self.compressed_image)
        if success:
            print(f"\n✅ Image successfully saved at: {output_path}")
        else:
            print("❌ Failed to save the image. Check the path and format.")

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    k = int(input("Enter the value of k: "))
    
    compressor = ImageCompression(image_path, k)
    compressor.image_read()
    compressor.image_split_into_rgb_channel()
    compressor.compute_svd()
    compressor.compress_image()
    compressor.reconstruct_channel_rgb_after_reducing_svd()
    compressor.merge_channel()
    compressor.display_image()
    
    output_path = input("Enter Output Path: ")
    compressor.save_compressed_image(output_path)
