import cv2
import numpy as np
from skimage.util import random_noise

def pepper(imagelocation):
    amountrange = 0.3
    # Load the image
    img = cv2.imread(imagelocation)

    # Add salt-and-pepper noise to the image.
    noise_img = random_noise(img, mode='pepper',amount=amountrange)

    # The above function returns a floating-point image
    # on the range [0, 1], thus we changed it to 'uint8'
    # and from [0,255]
    noise_img = np.array(255*noise_img, dtype = 'uint8')
    return noise_img
    # Display the noise image
    # cv2.imshow('blur',noise_img)
    # cv2.waitKey(0)
    # cv2.imwrite('C:/Users/fredd/Documents/GitHub/Prism-gui-image-augment/noises/image.png',Image)
    # img.save(filename ="peppernoise.jpeg")

# peppernoise(r"C:\Users\fredd\Documents\GitHub\Prism-gui-image-augment\images\image-25.jpg",0.3)