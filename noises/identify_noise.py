import cv2
import numpy as np



noise_types = ['gaussian', 'salt', 'pepper', 'poisson', 'speckle', 'localvar', 's&p', 'periodic', 'blobs', 'text']
noisy_images = []

def identify_image_in_noise(location):
    print(location)
    img = cv2.imread(location, 0)
    for noise_type in noise_types:
        if noise_type == 'gaussian':
            noisy_img = cv2.GaussianBlur(img, (5, 5), 0)
            noisy_images.append(noisy_img)
        elif noise_type == 'salt':
            noisy_img = img.copy()
            cv2.randu(noisy_img, 0, 255)
            noisy_img[noisy_img > 245] = 255
            noisy_images.append(noisy_img)
        elif noise_type == 'pepper':
            noisy_img = img.copy()
            cv2.randu(noisy_img, 0, 255)
            noisy_img[noisy_img < 10] = 0
            noisy_images.append(noisy_img)
        elif noise_type == 'poisson':
            noisy_img = np.random.poisson(img / 10.0) * 10
            noisy_images.append(noisy_img)
        elif noise_type == 'speckle':
            noisy_img = img.copy()
            cv2.randn(noisy_img, 0, 50)
            noisy_img = img + img * noisy_img / 100.0
            noisy_images.append(noisy_img)
        elif noise_type == 'localvar':
            noisy_img = img.copy()
            noisy_img = cv2.filter2D(noisy_img, -1, np.ones((3,3))/9.0)
            noisy_images.append(noisy_img)
        # elif noise_type == 's&p':
        #     noisy_img = img.copy()
        #     num_salt = np.ceil(0.05 * img.size * 2)
        #     coords = [np.random.randint(0, i-1, int(num_salt))
        #             for i in img.shape]
        #     noisy_img[coords] = 255
        #     num_pepper = np.ceil(0.05 * img.size * 2)
        #     coords = [np.random.randint(0, i-1, int(num_pepper))
        #             for i in img.shape]
        #     noisy_img[coords] = 0
        #     noisy_images.append(noisy_img)
        elif noise_type == 'periodic':
            noisy_img = img.copy()
            for i in range(10, noisy_img.shape[1], 50):
                noisy_img[:, i:i+10] = 255 - noisy_img[:, i:i+10]
            noisy_images.append(noisy_img)
        elif noise_type == 'blobs':
            noisy_img = np.zeros_like(img)
            cv2.circle(noisy_img, (150, 150), 100, 255, -1)
            cv2.circle(noisy_img, (350, 150), 100, 255, -1)
            cv2.circle(noisy_img, (250, 350), 100, 255, -1)
            noisy_img = cv2.GaussianBlur(noisy_img, (25, 25), 0)
            noisy_images.append(noisy_img)
        elif noise_type == 'text':
            noisy_img = img.copy()
            cv2.putText(noisy_img, 'OpenCV', (150, 300),cv2.FONT_HERSHEY_SIMPLEX, 5, 255, 10)
            noisy_images.append(noisy_img)
    print(len(noisy_images))

    for i, noisy_img in enumerate(noisy_images):
        diff = cv2.absdiff(img, noisy_img)
        ret, thresh = cv2.threshold(diff, 10, 255, cv2.CV_32F)
        nonzero = cv2.countNonZero(thresh)
        if nonzero > 0:
            print('Image', i+1, 'contains noise')
        else:
            print('Image', i+1, 'is noise-free')
identify_image_in_noise("D:/Prism-gui-image-augment/output/flimgrain1.jpg")