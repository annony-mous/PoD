import os
import numpy as np
from PIL import Image

def compute_skewness_kurtosis(image_folder):
    image_skews = []
    image_kurts = []

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

                sk_k = np.sum(((img_arr - m_k) / s_k) ** 3) / P
                kr_k = np.sum(((img_arr - m_k) / s_k) ** 4) / P

            # Color image (RGB)
            elif img_arr.ndim == 3:
                m, n, c = img_arr.shape
                P = m * n * c
                m_k = np.sum(img_arr) / P
                s_k = np.sqrt(np.sum((img_arr - m_k) ** 2) / (P - 1))

                sk_k = np.sum(((img_arr - m_k) / s_k) ** 3) / P
                kr_k = np.sum(((img_arr - m_k) / s_k) ** 4) / P

            else:
                continue  # skip unsupported formats

            image_skews.append(sk_k)
            image_kurts.append(kr_k)

    # Dataset-level statistics
    sk_d = np.mean(image_skews)
    kr_d = np.mean(image_kurts)

    return sk_d, kr_d


if __name__ == "__main__":
    folder_path = "Dataset/Dataset 2"  # Replace with your image folder path
    skewness, kurtosis = compute_skewness_kurtosis(folder_path)
    print(f"Dataset Skewness: {skewness}, Dataset Kurtosis: {kurtosis}")