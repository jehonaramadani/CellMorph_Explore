import numpy as np
import cv2
import os
from skimage.draw import disk
np.random.seed(42)

def generate_synthetic_cells(output_dir="data/synthetic_cells", n=100):
    os.makedirs(output_dir, exist_ok=True)
 
    if os.listdir(output_dir):
        print("Synthetic images already exist. Skipping generation.")
        return

    for i in range(n):
        img = np.zeros((128, 128), dtype=np.uint8)
        radius = np.random.randint(10, 30)
        center = (np.random.randint(40, 88), np.random.randint(40, 88))
        rr, cc = disk(center, radius)
        img[rr, cc] = 255
        noise = np.random.normal(0, 20, img.shape).astype(np.uint8)
        img = cv2.add(img, noise)
        cv2.imwrite(f"{output_dir}/cell_{i:03d}.png", img)
  