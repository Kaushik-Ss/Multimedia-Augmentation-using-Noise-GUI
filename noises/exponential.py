import cv2
import numpy as np

def exponential(image_path):
    # Check if GPU is available
    if cv2.cuda.getCudaEnabledDeviceCount() > 0:
        # Load image onto GPU
        gpu_image = cv2.cuda.imread(image_path)
        # Generate random values from exponential distribution on GPU
        peak = 1
        gpu_random_vals = cv2.cuda_GpuMat(gpu_image.size(), cv2.CV_32FC1)
        cv2.cuda.randn(gpu_random_vals, 0.0, peak)
        gpu_random_vals = gpu_random_vals * (gpu_image / 255.0)
        # Scale the random values to the range [0, 255] on GPU
        gpu_scaled_vals = cv2.cuda_GpuMat(gpu_image.size(), cv2.CV_32FC1)
        cv2.cuda.normalize(gpu_random_vals, gpu_scaled_vals, 0, 255, cv2.NORM_MINMAX, -1)
        # Convert the values to unsigned 8-bit integers on GPU
        gpu_noisy_image = cv2.cuda_GpuMat(gpu_image.size(), cv2.CV_8UC1)
        gpu_scaled_vals.convertTo(gpu_noisy_image, cv2.CV_8UC1)
        # Download the noisy image from GPU
        noisy_image = gpu_noisy_image.download()
    else:
        # Load the image
        image = cv2.imread(image_path)
        # Generate random values from exponential distribution on CPU
        peak = 1
        random_vals = np.random.exponential(scale=image / 255.0 * peak)
        # Scale the random values to the range [0, 255] on CPU
        scaled_vals = random_vals / np.max(random_vals) * 255
        # Convert the values to unsigned 8-bit integers on CPU
        noisy_image = scaled_vals.astype(np.uint8)
    return noisy_image

# cv2.imwrite('exponential.jpeg',exponential("images\image-3.jpg"))

# idk code 

# def exponential(image_path):
#     # Load the image
#     image = cv2.imread(image_path)
#     # Generate random values from exponential distribution
#     peak = 1
#     random_vals = np.random.exponential(scale=image / 255.0 * peak)
#     # Scale the random values to the range [0, 255]
#     scaled_vals = random_vals / np.max(random_vals) * 255
#     # Convert the values to unsigned 8-bit integers
#     noisy_image = scaled_vals.astype(np.uint8)
#     return noisy_image
