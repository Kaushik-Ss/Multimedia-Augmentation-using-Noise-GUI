import numpy as np
import cv2


def identify(noised_image_loc)

    identified_noise=[]
    img = cv2.imread(noised_image_loc, 0)

    # Set a threshold value to identify the number of black pixels
    threshold_value = 5

    # Count the number of black pixels in the image
    num_black_pixels = np.sum(img <= threshold_value)

    # Calculate the percentage of black pixels in the image
    percentage_black_pixels = (num_black_pixels / (img.shape[0] * img.shape[1])) * 100

    # If the percentage is above a certain threshold, then it is pepper noise
    if percentage_black_pixels > 1:
        identified_noise.append('Pepper noise detected')

    # Calculate the variance of the image
    img_var = np.var(img)

    # If the variance is less than a certain threshold, then it is Poisson noise
    if img_var < 10:
        identified_noise.append('Poisson noise detected')


    # Calculate the mean and standard deviation of the image
    img_mean, img_std = cv2.meanStdDev(img)

    # Calculate the skewness of the image
    img_skew = np.sum(((img - img_mean) / img_std) ** 3) / (img.shape[0] * img.shape[1])

    # If the skewness is greater than a certain threshold, then it is Rayleigh noise
    if img_skew > 0.5:
        identified_noise.append('Rayleigh noise detected')


    # Calculate the range of the image
    img_range = np.max(img) - np.min(img)

    # If the range is less than a certain threshold, then it is uniform noise
    if img_range < 10:
        identified_noise.append('Uniform noise detected')


    # Set a threshold value to identify the number of black and white pixels
    threshold_value = 5

    # Count the number of black and white pixels in the image
    num_black_pixels = np.sum(img <= threshold_value)
    num_white_pixels = np.sum(img >= 255 - threshold_value)

    # Calculate the percentage of black and white pixels in the image
    percentage_black_pixels = (num_black_pixels / (img.shape[0] * img.shape[1])) * 100
    percentage_white_pixels = (num_white_pixels / (img.shape[0] * img.shape[1])) * 100

    # If the percentage of black and white pixels is above a certain threshold, then it is impulse noise
    if percentage_black_pixels > 1 and percentage_white_pixels > 1:
        identified_noise.append('Impulse noise detected')


    # Calculate the mean and standard deviation of the image
    img_mean, img_std = cv2.meanStdDev(img)

    # If the standard deviation is greater than a certain threshold, then it is Gaussian noise
    if img_std > 10:
        identified_noise.append('Gaussian noise detected')


    # Perform a Fourier transform on the image
    f = np.fft.fft2(img)

    # Shift the zero-frequency component to the center of the spectrum
    fshift = np.fft.fftshift(f)

    # Calculate the magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    # Calculate the mean value of the magnitude spectrum
    mean_magnitude_spectrum = np.mean(magnitude_spectrum)

    # If the mean value is greater than a certain threshold, then it is periodic noise
    if mean_magnitude_spectrum > 10:
        identified_noise.append('Periodic noise detected')



    # Calculate the mean and standard deviation of the Laplacian of the image
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    mean, std = cv2.meanStdDev(laplacian)

    # If the standard deviation is greater than a certain threshold, then it is speckle noise
    if std > 10:
        identified_noise.append('Speckle noise detected')

    # Calculate the gradient of the image
    gradient = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)

    # Calculate the mean and standard deviation of the gradient
    gradient_mean, gradient_std = cv2.meanStdDev(gradient)

    # If the standard deviation is greater than a certain threshold, then it is anisotropic noise
    if gradient_std > 10:
        identified_noise.append('Anisotropic noise detected')

    # Calculate the Laplacian of the image
    laplacian = cv2.Laplacian(img, cv2.CV_64F)

    # Calculate the mean and standard deviation of the Laplacian
    laplacian_mean, laplacian_std = cv2.meanStdDev(laplacian)

    # If the standard deviation is greater than a certain threshold, then it is exponential noise
    if laplacian_std > 10:
        identified_noise.append('Exponential noise detected')

    # Calculate the mean and standard deviation of the Laplacian of the image
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    mean, std = cv2.meanStdDev(laplacian)

    # If the standard deviation is greater than a certain threshold, then it is film grain noise
    if std > 10:
        identified_noise.append('Film grain noise detected')


    # Calculate the Laplacian of the image
    laplacian = cv2.Laplacian(img, cv2.CV_64F)

    # Calculate the mean and standard deviation of the Laplacian
    laplacian_mean, laplacian_std = cv2.meanStdDev(laplacian)

    # If the standard deviation is greater than a certain threshold, then it is gamma noise
    if laplacian_std > 10:
        identified_noise.append('Gamma noise detected')


    return identified_noise

print(identify('speckle1.jpg'))