# import numpy as np
# import cv2
# def rayleigh(image):
#     img = cv2.imread(image)
#     PEAK=1
#     return np.random(img / 255.0 * PEAK) / PEAK * 255
# # image = cv2.imread("pic1.jpeg")  # need a rescale to be more realistic
# # cv2.imwrite('rayleigh.jpeg',rayleigh_func("./images/pic1.jpeg"))

import cv2
import numpy as np

def rayleigh(img,value):
    scale = value*100
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    noise = np.random.rayleigh(scale, size=image.shape).astype(np.float32)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image