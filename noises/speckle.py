import cv2
import numpy as np

def speckle(imagelocation,value):
    img = cv2.imread(imagelocation, 0)
    noise_level = value
    noise = np.random.normal(loc=1, scale=noise_level, size=img.shape)
    noisy_img = img * noise
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    return noisy_img