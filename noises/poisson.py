import numpy as np
import cv2
def poisson(imagelocation,value):
    image = cv2.imread(imagelocation)
    PEAK=1-value
    return np.random.poisson(image / 255.0 * PEAK) / PEAK * 255

# cv2.imwrite('poiss.jpeg',poisson_func("images\image-4.jpg"))