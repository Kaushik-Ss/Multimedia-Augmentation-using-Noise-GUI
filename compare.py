import cv2
import numpy as np
from pathlib import Path
 
# open file

file1=r"E:\prism gui image augment\images\image-1.jpg"
file2=r"E:\prism gui image augment\images\image-1.jpg"
# getting file size

from math import log10, sqrt
import cv2
import numpy as np
  
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
  
original = cv2.imread(file1)
compressed = cv2.imread(file2, 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")
print("The larger the value of PSNR, the more efficient is a corresponding compression or filter method.")
       




# load the input images
img1 = cv2.imread(file1)
img2 = cv2.imread(file2)

# convert the images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:",error)

cv2.imshow("difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows() 