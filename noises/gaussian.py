import numpy as np
import cv2
import random
def gaussian(imagelocation):
    image = cv2.imread(imagelocation)
    PEAK=1
    return np.random.normal(image / 30 * PEAK) / PEAK * 100
# image = cv2.imread("pic1.jpeg")  # need a rescale to be more realistic

# cv2.imwrite('gaussian.jpeg',gaussian_func("images\image-3.jpg"))
 