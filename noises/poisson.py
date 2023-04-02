import numpy as np
import cv2
try:
    import cupy as cp
    USE_GPU = True
except ImportError:
    USE_GPU = False

def poisson(imagelocation):
    image = cv2.imread(imagelocation)
    print(USE_GPU)
    if USE_GPU: 
        # Transfer the image to the GPU
        image_gpu = cp.asarray(image)
        # Generate the Poisson noise on the GPU
        PEAK = 1
        noise_gpu = cp.random.poisson(image_gpu / 255.0 * PEAK) / PEAK * 255
        # Transfer the noise back to the CPU
        noise = cp.asnumpy(noise_gpu)
    else:
        # Generate the Poisson noise on the CPU
        PEAK = 1
        noise = np.random.poisson(image / 255.0 * PEAK) / PEAK * 255

    return noise


# cv2.imwrite('poiss.jpeg',poisson_func("images\image-4.jpg"))