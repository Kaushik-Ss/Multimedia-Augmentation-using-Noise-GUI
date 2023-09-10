import random
import cv2
  
def impulse(imagelocation,value):
    img = cv2.imread(imagelocation,cv2.IMREAD_GRAYSCALE)
    row , col = img.shape
    
    number_of_pixels=300+((value*100)*1000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 255
        
        y_coord_n=random.randint(0, row - 1)
        x_coord_n=random.randint(0, col - 1)
        img[y_coord_n][x_coord_n] = 0
        
          
    return img

# cv2.imwrite('impulse.jpeg',impulse("images\image-3.jpg"))