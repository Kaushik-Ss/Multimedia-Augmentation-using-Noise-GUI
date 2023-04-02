# import cv2
# import numpy as np


# def anisotropic(imagelocation):
#     # Load the image
#     img = cv2.imread(imagelocation)

#     # Define the noise level and the scale of the noise
#     noise_level = 0.1
#     noise_scale = 10

#     # Generate anisotropic noise
#     noise = np.zeros_like(img)
#     for i in range(3):
#         noise[:, :, i] = np.random.normal(loc=0, scale=noise_level*img[:, :, i].std(), size=img[:, :, i].shape)
#         noise[:, :, i] = cv2.GaussianBlur(noise[:, :, i], ksize=(noise_scale, noise_scale), sigmaX=0)

#     # Add the noise to the image
#     noisy_img = np.clip(img + noise, 0, 255).astype(np.uint8)
#     return noisy_img
#     # Display the noisy image
#     # cv2.imshow('Noisy Image', noisy_img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()


import numpy as np
import cv2
import time

def anisotropic(imagelocation):
    img = cv2.imread(imagelocation, 0)
    mean = 0
    stddev = 50
    noise = np.random.normal(mean, stddev, img.shape)
    if cv2.cuda.getCudaEnabledDeviceCount() > 0: 
        img_gpu = cv2.cuda_GpuMat(img)
        noise_gpu = cv2.cuda_GpuMat(noise.astype(np.float32))
        cv2.cuda.add(img_gpu, noise_gpu, img_gpu)
        noisy_img = img_gpu.download()
    else:
        noisy_img = img + noise.astype(np.uint8)

    return noisy_img
