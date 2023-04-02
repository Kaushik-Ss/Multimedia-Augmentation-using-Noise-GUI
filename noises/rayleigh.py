# import numpy as np
# import cv2
# def rayleigh(image):
#     img = cv2.imread(image)
#     PEAK=1
#     return np.random(img / 255.0 * PEAK) / PEAK * 255
# # image = cv2.imread("pic1.jpeg")  # need a rescale to be more realistic
# # cv2.imwrite('rayleigh.jpeg',rayleigh_func("./images/pic1.jpeg"))

import cv2
import numpy as np
import numba.cuda as cuda
import math

def add_rayleigh_noise(img):
    scale = 50
    # why grayscale??????????
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    if cuda.is_available():
        h, w = image.shape
        threadsperblock = (32, 32)
        blockspergrid_x = math.ceil(w / threadsperblock[0])
        blockspergrid_y = math.ceil(h / threadsperblock[1])
        blockspergrid = (blockspergrid_x, blockspergrid_y)

        @cuda.jit
        def add_rayleigh_kernel(image, noise, scale):
            x, y = cuda.grid(2)
            if x < image.shape[1] and y < image.shape[0]:
                noise[y, x] = np.random.rayleigh(scale)

            cuda.syncthreads()

            if x < image.shape[1] and y < image.shape[0]:
                noisy_image = image[y, x] + noise[y, x]
                image[y, x] = np.clip(noisy_image, 0, 255)

        noise = cuda.device_array_like(image)
        add_rayleigh_kernel[blockspergrid, threadsperblock](image, noise, scale)
        noisy_image = image.copy_to_host()

        return noisy_image

    else:
        noise = np.random.rayleigh(scale, size=image.shape).astype(np.float32)
        noisy_image = image + noise
        noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
        return noisy_image
