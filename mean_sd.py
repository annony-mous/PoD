import os
import numpy as np
from PIL import Image

def compute_mean_std(image_folder):
    image_means = []
    image_stds = []

    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            path = os.path.join(image_folder, filename)

            # Load image
            img = Image.open(path)
            img_arr = np.array(img).astype(np.float64)

            # Grayscale image
            if img_arr.ndim == 2:
                P = img_arr.size
                m_k = np.sum(img_arr) / P
                s_k = np.sqrt(np.sum((img_arr - m_k) ** 2) / (P - 1))

            # Color image (RGB)
            elif img_arr.ndim == 3:
                # print(f"Processing color image: {filename}")
                m, n, c = img_arr.shape
                P = m * n * c
                m_k = np.sum(img_arr) / P
                s_k = np.sqrt(np.sum((img_arr - m_k) ** 2) / (P - 1))

            else:
                continue  # skip unsupported formats

            image_means.append(m_k)
            image_stds.append(s_k)

    # Dataset-level statistics
    m_d = np.mean(image_means)
    s_d = np.mean(image_stds)

    return m_d, s_d


if __name__ == "__main__":
    folder_path = "Dataset/Dataset 2"  # Replace with your image folder path
    mean, std = compute_mean_std(folder_path)
    print(f"Dataset Mean: {mean}, Dataset Std Dev: {std}")