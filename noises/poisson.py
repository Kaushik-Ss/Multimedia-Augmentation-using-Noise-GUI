import numpy as np
import cv2
import random
def poisson_func(imagelocation):
    image = cv2.imread(imagelocation)
    PEAK=1
    return np.random.poisson(image / 255.0 * PEAK) / PEAK * 255

# cv2.imwrite('poiss.jpeg',poisson_func("images\image-4.jpg"))