import os
import numpy as np
from skimage import io, img_as_float

# ---------------------------------------------------
# Load images
# ---------------------------------------------------
def load_images(dataset_folder):
    images = []
    names = []
    for fname in os.listdir(dataset_folder):
        if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            path = os.path.join(dataset_folder, fname)
            img = img_as_float(io.imread(path))
            images.append(img)
            names.append(fname)
    return images, names


# ---------------------------------------------------
# Compute Z-score and IQR based outliers
# ---------------------------------------------------
def detect_outliers(images, image_names, z_thresh=3.0):
    image_means = np.array([img.mean() for img in images])

    m_d = image_means.mean()
    s_d = image_means.std(ddof=1)

    outliers = []

    for img, name, m_k in zip(images, image_names, image_means):

        # ---------- Z-score ----------
        zs_k = (m_k - m_d) / s_d if s_d > 0 else 0

        # ---------- IQR ----------
        pixels = img.flatten()
        Q1 = np.percentile(pixels, 25)
        Q3 = np.percentile(pixels, 75)
        IQR = Q3 - Q1

        lbiqr = Q1 - 5 * IQR
        ubiqr = Q3 + 5 * IQR

        # Pixel-level violation
        pixel_outlier = np.any((pixels < lbiqr) | (pixels > ubiqr))

        # Final decision
        if abs(zs_k) > z_thresh or pixel_outlier:
            outliers.append({
                "image": name,
                "z_score": zs_k,
                "IQR": IQR
            })

    return outliers


# ---------------------------------------------------
# Example usage
# ---------------------------------------------------
if __name__ == "__main__":
    dataset_path = "Dataset/Dataset 3"  # change path if needed

    images, names = load_images(dataset_path)
    outliers = detect_outliers(images, names)

    print(f"Detected {len(outliers)} outliers:\n")
    for o in outliers:
        print(o)
