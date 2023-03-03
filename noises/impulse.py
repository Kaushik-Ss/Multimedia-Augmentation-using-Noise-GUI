import random
import cv2
  
def impulse(imagelocation):
    img = cv2.imread(imagelocation,cv2.IMREAD_GRAYSCALE)
    row , col = img.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 0
          
    return img

# cv2.imwrite('impulse.jpeg',impulse("images\image-3.jpg"))