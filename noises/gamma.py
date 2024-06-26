import numpy as np
import cv2
def gamma(image,value):
    image = cv2.imread(image)
    PEAK=1-value
    return np.random.gamma(image / 255.0 * PEAK) / PEAK * 255

# cv2.imwrite('gamma.jpeg',gamma_func("images\image-3.jpg"))