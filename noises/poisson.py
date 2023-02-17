import numpy as np
import cv2
import random
# def poisson_func(image):
#     PEAK=1
#     return np.random.poisson(image / 255.0 * PEAK) / PEAK * 255
# image = cv2.imread("")  # need a rescale to be more realistic
# cv2.imwrite('poisson.jpeg',poisson_func(image))



def poissonimage(image):
    peak = 1
    return np.random.poisson(image / 255.0 * peak) / peak * 255
image = cv2.imread("../images/image-1.jpg")
cv2.imwrite('poisson.jpeg',poissonimage(image))