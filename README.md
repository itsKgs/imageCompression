
# 📦 SVD-Based Image Compression

A Python project that performs image compression using **Singular Value Decomposition (SVD)** on the RGB channels of a color image.

---

## 📌 Features

- Reads and displays any color image
- Splits image into Red, Green, and Blue channels
- Applies SVD on each channel
- Reconstructs the image using the top `k` singular values
- Displays and saves the compressed image

---

## 🖼️ Sample Output

- Original and compressed image comparison (shown via OpenCV GUI)
- Matrix shape and values printed for debugging and learning purposes

---

## 🧠 How It Works

1. Image is split into RGB channels.
2. SVD is performed on each channel.
3. Each channel is reconstructed using only the top `k` singular values.
4. The channels are merged to create the compressed image.

---

## 📁 Project Structure

```
svd_image_compression/
├── image_compression.py   # Main Python script
├── example.jpg            # (Optional) Sample input image
└── README.md              # This file
```

---

## 🛠 Requirements

Install required packages using:

```bash
pip install numpy opencv-python
```

---

## 🚀 How to Run

```bash
python image_compression.py
```

Then follow the prompts:
- Enter the path to your input image
- Enter the value of `k` (number of singular values to retain)
- Provide a save path for the compressed output

---

## ✍️ Example Usage

```
Enter the image path: example.jpg
Enter the value of k: 50
Enter Output Path: ./output/
```

---

## 📊 What is SVD Compression?

SVD helps reduce image size while retaining important features:
- Lower `k` means more compression (less detail).
- Higher `k` retains more image quality.

---

## 📷 Sample Compression (k = 50 vs. k = 200)

| k Value | File Size | Quality |
|--------|-----------|---------|
| 50     | Smaller   | Blurry  |
| 200    | Larger    | Clear   |

---

