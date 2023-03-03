# import numpy as np
# import cv2
# def rayleigh(image):
#     img = cv2.imread(image)
#     PEAK=1
#     return np.random(img / 255.0 * PEAK) / PEAK * 255
# # image = cv2.imread("pic1.jpeg")  # need a rescale to be more realistic
# # cv2.imwrite('rayleigh.jpeg',rayleigh_func("./images/pic1.jpeg"))

import cv2
import numpy as np

def add_rayleigh_noise(img):
    scale = 50
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    """
    Add Rayleigh noise to an image.
    
    Args:
        image (numpy.ndarray): Input image.
        scale (float): Scale parameter of the Rayleigh distribution.
    
    Returns:
        numpy.ndarray: Noisy image.
    """
    # Generate noise with Rayleigh distribution
    noise = np.random.rayleigh(scale, size=image.shape).astype(np.float32)
    
    # Add noise to image
    noisy_image = image + noise
    
    # Clip pixel values to [0, 255]
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    
    return noisy_image



