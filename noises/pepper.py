import cv2
import numpy as np
import random

def pepper(img_path, value):
    salt_prob=pepper_prob=value
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    num_salt = int(height * width * salt_prob)
    num_pepper = int(height * width * pepper_prob)

    for _ in range(num_salt):
        y, x = random.randint(0, height - 1), random.randint(0, width - 1)
        img[y, x] = [255, 255, 255]  

    for _ in range(num_pepper):
        y, x = random.randint(0, height - 1), random.randint(0, width - 1)
        img[y, x] = [0, 0, 0]  
    return img
