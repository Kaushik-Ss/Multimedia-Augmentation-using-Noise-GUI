import numpy as np
import cv2
import random
def rayleigh_func(image):
    image = cv2.imread(image)
    PEAK=1
    return np.random.(image / 255.0 * PEAK) / PEAK * 255
# image = cv2.imread("pic1.jpeg")  # need a rescale to be more realistic
cv2.imwrite('rayleigh.jpeg',rayleigh_func("./images/pic1.jpeg"))