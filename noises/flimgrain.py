import cv2
import numpy as np

def flimgrain(imagelocation,value):
    img = cv2.imread(imagelocation)
    noise_level = round(value/10,2)
    noise = np.random.normal(loc=0, scale=noise_level, size=img.shape)
    noisy_img = np.clip(img.astype(np.float32) + noise*255, 0, 255).astype(np.uint8)
    return noisy_img
