import numpy as np
import cv2
def gaussian(imagelocation,value):
    image = cv2.imread(imagelocation)
    PEAK=1-value
    # idk why 30
    return np.random.normal(image / 30 * PEAK) / PEAK * 100

# cv2.imwrite('gaussian.jpeg',gaussian_func("images\image-3.jpg"))
 