import cv2
import numpy as np


def periodic(imagelocation):
    # Load the image
    img = cv2.imread(imagelocation, 0)

    # Define the noise level and the frequency of the noise
    noise_level = 0.1
    noise_freq = 0.05

    # Generate periodic noise
    h, w = img.shape
    y, x = np.ogrid[0:h, 0:w]
    noise = np.sin(2*np.pi*noise_freq*x + np.pi*noise_freq*y)
    noise = np.clip(noise, -1, 1) * noise_level
    noisy_img = np.clip(img.astype(np.float32) + noise*255, 0, 255).astype(np.uint8)

    return noisy_img
    # Display the noisy image
    # cv2.imshow('Noisy Image', noisy_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
