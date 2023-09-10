import cv2
import numpy as np
from skimage.util import random_noise

def pepper(imagelocation,value):
    amountrange = value
    img = cv2.imread(imagelocation)
    noise_img = random_noise(img, mode='pepper',amount=amountrange)
    noise_img = np.array(255*noise_img, dtype = 'uint8')
    return noise_img

# peppernoise(r"C:\Users\fredd\Documents\GitHub\Prism-gui-image-augment\images\image-25.jpg",0.3)