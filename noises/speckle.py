import math
import cv2
import numpy as np
import numba.cuda as cuda

def speckle(imagelocation):
    img = cv2.imread(imagelocation, 0)
    noise_level = 0.1
    
    if cuda.is_available():
        h, w = img.shape
        threadsperblock = (32, 32)
        blockspergrid_x = math.ceil(w / threadsperblock[0])
        blockspergrid_y = math.ceil(h / threadsperblock[1])
        blockspergrid = (blockspergrid_x, blockspergrid_y)

        @cuda.jit
        def speckle_kernel(img, noise, noise_level):
            x, y = cuda.grid(2)
            if x < img.shape[1] and y < img.shape[0]:
                noise[y, x] = np.random.normal(loc=1, scale=noise_level)

            cuda.syncthreads()

            if x < img.shape[1] and y < img.shape[0]:
                noisy_img = img[y, x] * noise[y, x]
                img[y, x] = np.clip(noisy_img, 0, 255)

        noise = cuda.device_array_like(img)
        speckle_kernel[blockspergrid, threadsperblock](img, noise, noise_level)
        noisy_img = img.copy_to_host()
        return noisy_img

    else:
        noise = np.random.normal(loc=1, scale=noise_level, size=img.shape)
        noisy_img = img * noise
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
        return noisy_img
