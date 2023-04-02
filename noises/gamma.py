import numpy as np
import cv2
def gamma(image):
    img = cv2.imread(image)
    
    if cv2.cuda.getCudaEnabledDeviceCount() > 0:  # check if GPU is available
        img_gpu = cv2.cuda_GpuMat(img)

        # Split channels and convert to floating point type
        b_gpu, g_gpu, r_gpu = cv2.cuda.split(img_gpu)
        b_gpu = b_gpu.astype(np.float32) / 255.0
        g_gpu = g_gpu.astype(np.float32) / 255.0
        r_gpu = r_gpu.astype(np.float32) / 255.0

        # Apply gamma correction using CUDA functions
        gamma = 0.5
        b_gpu = cv2.cuda.pow(b_gpu, gamma) * 255.0
        g_gpu = cv2.cuda.pow(g_gpu, gamma) * 255.0
        r_gpu = cv2.cuda.pow(r_gpu, gamma) * 255.0

        # Merge channels and download result back to CPU
        img_gpu = cv2.cuda.merge([b_gpu, g_gpu, r_gpu])
        result = img_gpu.download()
    else:
        gamma = 0.5
        result = np.power(img / 255.0, gamma) * 255.0

    return result

# cv2.imwrite('gamma.jpeg',gamma_func("images\image-3.jpg"))