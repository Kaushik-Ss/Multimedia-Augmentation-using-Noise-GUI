# from wand.image import Image
  
# def uniformnoise(imagelocation):
#     attenuaterange = 0.9
#     with Image(filename = imagelocation) as img:
#         img.noise("uniform", attenuate = attenuaterange)
#         # img.save(filename ="uniformnoise.jpeg")
#     return img

# # uniformnoise(r"C:\Users\fredd\Documents\GitHub\Prism-gui-image-augment\images\image-28.jpg",0.9)


import numpy as np
import cv2
import time
from skimage.util import random_noise

def uniform(imagelocation,value):
    img = cv2.imread(imagelocation, 0)
    intensity = value
    noise = np.random.uniform(-intensity, intensity, img.shape)
    noisy_img = img + noise.astype(np.uint8)
    # cv2.imwrite('noisy_image_cv2.jpg', noisy_img)
    return noisy_img