import cv2
import numpy as np

def flimgrain(imagelocation):
    # Check if GPU is available
    # print(cv2.cuda.getCudaEnabledDeviceCount())
    # if cv2.cuda.getCudaEnabledDeviceCount() > 0:
    #     # Load image onto GPU
    #     gpu_img = cv2.cuda.imread(imagelocation)

    #     # Generate noise on GPU
    #     noise_level = 0.1
    #     gpu_noise = cv2.cuda_GpuMat(gpu_img.size(), cv2.CV_32FC1)
    #     cv2.cuda.randn(gpu_noise, 0.0, noise_level)

    #     # Add noise to image on GPU
    #     gpu_noisy_img = cv2.cuda.addWeighted(gpu_img, 1.0, gpu_noise, 255.0, 0.0, dtype=cv2.CV_32FC1)
    #     gpu_noisy_img.convertTo(gpu_noisy_img, cv2.CV_8UC3)

    #     # Download noisy image from GPU
    #     noisy_img = gpu_noisy_img.download()
    if True:
    # else:
        # Load image onto CPU
        img = cv2.imread(imagelocation)

        # Generate noise on CPU
        noise_level = 0.1
        noise = np.random.normal(loc=0, scale=noise_level, size=img.shape)

        # Add noise to image on CPU
        noisy_img = np.clip(img.astype(np.float32) + noise*255, 0, 255).astype(np.uint8)

        return noisy_img