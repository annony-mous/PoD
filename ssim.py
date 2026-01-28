import os
import random
import numpy as np
from skimage import io, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize

def load_images(dataset_folder):
    """
    Load all images in a folder as float arrays (0-1).
    """
    images = []
    for filename in os.listdir(dataset_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            path = os.path.join(dataset_folder, filename)
            img = io.imread(path)
            img_float = img_as_float(img)
            images.append(img_float)
    return images

def compute_dataset_ssim(images, num_references=5):
    """
    Compute SSIM of a dataset by comparing images with multiple reference images.
    Returns the average SSIM value.
    """
    if len(images) == 0:
        return None

    num_references = min(num_references, len(images))
    reference_indices = random.sample(range(len(images)), num_references)

    ssim_vals = []

    for ref_idx in reference_indices:
        ref_img = images[ref_idx]

        for img in images:
            # Resize to reference image if shapes differ
            if ref_img.shape != img.shape:
                img = resize(img, ref_img.shape, anti_aliasing=True)

            # Determine win_size for SSIM
            min_dim = min(ref_img.shape[:2])
            win_size = min(7, min_dim) if min_dim >= 7 else min_dim
            if win_size % 2 == 0:
                win_size -= 1  # SSIM requires odd win_size

            # Handle grayscale images
            if img.ndim == 2:
                ssim_val = ssim(ref_img, img, win_size=win_size, data_range=1.0)
            else:  # color image
                ssim_val = ssim(ref_img, img, channel_axis=-1, win_size=win_size, data_range=1.0)

            ssim_vals.append(ssim_val)

    return np.mean(ssim_vals)

if __name__ == "__main__":
    folder_path = "Dataset/Dataset 1"  # Replace with your dataset folder path
    images = load_images(folder_path)
    ssim_value = compute_dataset_ssim(images, num_references=5)
    print(f"Dataset SSIM value: {ssim_value:.4f}")
