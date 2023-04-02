import numpy as np
import cv2
def exponential(image):
    image = cv2.imread(image)
    PEAK=1
    return np.random.exponential(image / 255.0 * PEAK) / PEAK * 255

# cv2.imwrite('exponential.jpeg',exponential("images\image-3.jpg"))

# idk code 

# def exponential(image_path):
#     # Load the image
#     image = cv2.imread(image_path)
#     # Generate random values from exponential distribution
#     peak = 1
#     random_vals = np.random.exponential(scale=image / 255.0 * peak)
#     # Scale the random values to the range [0, 255]
#     scaled_vals = random_vals / np.max(random_vals) * 255
#     # Convert the values to unsigned 8-bit integers
#     noisy_image = scaled_vals.astype(np.uint8)
#     return noisy_image
