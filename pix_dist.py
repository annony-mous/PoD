import os
import numpy as np
from PIL import Image

def pixel_distribution(dataset_folder, num_bins=256):
    """
    Compute pixel distribution for a dataset of images.
    
    Args:
        dataset_folder (str): Path to the folder containing images.
        num_bins (int): Number of bins (default 256 for 8-bit images).
    
    Returns:
        hist_d (np.array): Normalized pixel distribution (probabilities).
    """
    # Initialize histogram
    hist_d = np.zeros(num_bins, dtype=np.float64)
    total_pixels = 0

    # Iterate over images in the folder
    for filename in os.listdir(dataset_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            path = os.path.join(dataset_folder, filename)

            # Load image
            img = Image.open(path)
            img_arr = np.array(img).astype(np.int32)

            # Grayscale image
            if img_arr.ndim == 2:
                # Flatten and count pixel intensities
                hist, _ = np.histogram(img_arr, bins=num_bins, range=(0, 255))
                hist_d += hist
                total_pixels += img_arr.size

            # Color image (RGB)
            elif img_arr.ndim == 3 and img_arr.shape[2] == 3:
                # Flatten all channels together
                flat_pixels = img_arr.reshape(-1)
                hist, _ = np.histogram(flat_pixels, bins=num_bins, range=(0, 255))
                hist_d += hist
                total_pixels += flat_pixels.size

    # Normalize to get probabilities
    if total_pixels > 0:
        hist_d = hist_d / total_pixels

    return hist_d

if __name__ == "__main__":
    folder_path = "Dataset/Dataset 2"  # Replace with your dataset path
    pixel_hist = pixel_distribution(folder_path)
    print("Pixel distribution probabilities (first 20 bins):", pixel_hist[:20])
