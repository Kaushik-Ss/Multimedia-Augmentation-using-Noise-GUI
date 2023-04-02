import cv2
import numpy as np
import numba.cuda as cuda

def periodic(imagelocation):
    img = cv2.imread(imagelocation, 0)
    noise_level = 0.1
    noise_freq = 0.05
    h, w = img.shape
    print(cuda.is_available())
    if cuda.is_available():
        x, y = cuda.grid(2)
        if x < h and y < w:
            noise = np.sin(2*np.pi*noise_freq*x + np.pi*noise_freq*y)
            noise = np.clip(noise, -1, 1) * noise_level
            noisy_img = np.clip(img.astype(np.float32) + noise*255, 0, 255).astype(np.uint8)
            return noisy_img
    else:
        y, x = np.ogrid[0:h, 0:w]
        noise = np.sin(2*np.pi*noise_freq*x + np.pi*noise_freq*y)
        noise = np.clip(noise, -1, 1) * noise_level
        noisy_img = np.clip(img.astype(np.float32) + noise*255, 0, 255).astype(np.uint8)
        return noisy_img