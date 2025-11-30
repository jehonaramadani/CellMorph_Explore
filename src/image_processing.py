import cv2
import numpy as np
from skimage.filters import gaussian
from skimage.measure import label, regionprops

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    blurred = gaussian(img, sigma=1)
    _, thresh = cv2.threshold((blurred * 255).astype(np.uint8), 50, 255, cv2.THRESH_BINARY)
    return thresh

def extract_features(binary_img):
    lbl = label(binary_img)
    props = regionprops(lbl)
    if not props:
        return None
    region = props[0]
    area = region.area
    perimeter = region.perimeter
    circularity = 4 * np.pi * area / (perimeter ** 2) if perimeter > 0 else 0
    return {
        "area": area,
        "perimeter": perimeter,
        "circularity": circularity
    }
