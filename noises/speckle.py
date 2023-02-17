import cv2
import numpy as np


def speckle(imagelocation):
    # Load the image
    img = cv2.imread(imagelocation, 0)

    # Define the noise level and the scale of the noise
    noise_level = 0.1

    # Generate speckle noise
    noise = np.random.normal(loc=1, scale=noise_level, size=img.shape)
    noisy_img = img * noise

    # Clip the pixel values to the valid range [0, 255]
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

    # Display the noisy image
    cv2.imshow('Noisy Image', noisy_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()