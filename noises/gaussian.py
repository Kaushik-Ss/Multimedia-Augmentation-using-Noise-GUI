import numpy as np
import cv2
import random
def gaussian_func(image):
    PEAK=1
    return np.random.normal(image / 255.0 * PEAK) / PEAK * 255
image = cv2.imread("pic1.jpeg")  # need a rescale to be more realistic
cv2.imwrite('gaussian.jpeg',gaussian_func(image))