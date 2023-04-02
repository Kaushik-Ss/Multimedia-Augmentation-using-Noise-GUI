import numpy as np
import cv2
def gaussian(imagelocation):
    img = cv2.imread(imagelocation)
    print(cv2.cuda.getCudaEnabledDeviceCount())
    if cv2.cuda.getCudaEnabledDeviceCount() > 0:  # check if GPU is available
        # img_gpu = cv2.cuda_GpuMat(img)
        # Split channels and convert to floating point type
        b_gpu, g_gpu, r_gpu = cv2.cuda.split(img_gpu)
        b_gpu = b_gpu.astype(np.float32) / 30.0
        g_gpu = g_gpu.astype(np.float32) / 30.0
        r_gpu = r_gpu.astype(np.float32) / 30.0
        # Apply Gaussian noise using CUDA functions
        mean = 0
        stddev = 1
        noise_gpu = cv2.cuda.randn(img_gpu.size(), dtype=cv2.CV_32FC1) * stddev + mean
        b_gpu = cv2.cuda.addWeighted(b_gpu, 1.0, noise_gpu, 1.0, 0.0)
        g_gpu = cv2.cuda.addWeighted(g_gpu, 1.0, noise_gpu, 1.0, 0.0)
        r_gpu = cv2.cuda.addWeighted(r_gpu, 1.0, noise_gpu, 1.0, 0.0)
        # Convert back to 8-bit unsigned integer type and download result back to CPU
        b_gpu = cv2.cuda.normalize(b_gpu, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        g_gpu = cv2.cuda.normalize(g_gpu, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        r_gpu = cv2.cuda.normalize(r_gpu, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        img_gpu = cv2.cuda.merge([b_gpu, g_gpu, r_gpu])
        result = img_gpu.download()
    else:
        mean = 0
        stddev = 1
        noise = np.random.normal(mean, stddev, img.shape).astype(np.float32)
        result = np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)

    return result

# cv2.imwrite('gaussian.jpeg',gaussian_func("images\image-3.jpg"))
 