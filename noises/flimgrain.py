import cv2
import numpy as np

def flimgrain(imagelocation):
    # Load the image
    img = cv2.imread(imagelocation)
    
    # Define the noise level and the scale of the noise
    noise_level = 0.1

    # Generate film grain noise
    noise = np.random.normal(loc=0, scale=noise_level, size=img.shape)
    noisy_img = np.clip(img.astype(np.float32) + noise*255, 0, 255).astype(np.uint8)

    return noisy_img
    # Display the noisy image
    # cv2.imshow('Noisy Image', noisy_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
