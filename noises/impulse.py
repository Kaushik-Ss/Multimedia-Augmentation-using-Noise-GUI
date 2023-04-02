import random
import cv2
  
def impulse(imagelocation):
    img = cv2.imread(imagelocation,cv2.IMREAD_GRAYSCALE)
    row , col = img.shape
    number_of_pixels = random.randint(300, 10000)
    
    if cv2.cuda.getCudaEnabledDeviceCount() > 0:
        # use GPU if available
        img_gpu = cv2.cuda_GpuMat(img)
        for i in range(number_of_pixels):
            y_coord=random.randint(0, row - 1)
            x_coord=random.randint(0, col - 1)
            img_gpu.row(y_coord).col(x_coord)[:] = 255
        number_of_pixels = random.randint(300 , 10000)
        for i in range(number_of_pixels):
            y_coord=random.randint(0, row - 1)
            x_coord=random.randint(0, col - 1)
            img_gpu.row(y_coord).col(x_coord)[:] = 0
        return img_gpu.download()
    else:
        # use CPU if GPU not available
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