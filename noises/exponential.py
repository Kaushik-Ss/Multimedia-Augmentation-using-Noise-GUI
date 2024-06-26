import numpy as np
import cv2
def exponential(image,value):
    image = cv2.imread(image)
    PEAK=1-value
    return np.random.exponential(image / 255.0 * PEAK) / PEAK * 255

# cv2.imwrite('exponential.jpeg',exponential("images\image-3.jpg"))