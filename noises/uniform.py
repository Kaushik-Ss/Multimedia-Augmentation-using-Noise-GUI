import numpy as np
import cv2

def uniform(imagelocation,value):
    img = cv2.imread(imagelocation, 0)
    intensity = value
    noise = np.random.uniform(-intensity, intensity, img.shape)
    noisy_img = img + noise.astype(np.uint8)
    return noisy_img