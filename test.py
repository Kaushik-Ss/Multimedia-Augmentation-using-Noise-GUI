import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('speckle1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply edge detection to detect salt and pepper noise
edges = cv2.Canny(img, 100, 200)
edge_density = np.sum(edges) / (img.shape[0] * img.shape[1])
if edge_density < 0.01:
    print('Salt & Pepper noise detected')

# Apply Fourier transform to detect periodic noise
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
peak_intensity = np.max(magnitude_spectrum[1:])
if peak_intensity > 60:
    print('Periodic noise detected')

# Compute variance and mean to detect Gaussian or Poisson noise
variance = np.var(img)
mean = np.mean(img)
if variance > 100 and mean < 150:
    print('Gaussian noise detected')
elif variance < 100 and mean > 150:
    print('Poisson noise detected')





import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply a median filter to remove noise
img = cv2.medianBlur(img, 5)

# Compute the difference between the filtered image and the original image
diff = cv2.absdiff(img, cv2.GaussianBlur(img, (5,5), 0))

# Analyze the histogram of the difference image to identify the type of noise
hist, bins = np.histogram(diff.ravel(), 256, [0,256])

# Plot the histogram
plt.plot(hist)
plt.show()

# Identify the type of noise
if hist[0] > 10000:
    print("Salt and pepper noise")
elif hist[-1] > 10000:
    print("Gaussian noise")
else:
    print("No noise detected")
