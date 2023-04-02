import cv2
import numpy as np
from skimage.util import random_noise

def pepper(imagelocation):
    amountrange = 0.3
    img = cv2.imread(imagelocation)
    noise_img = random_noise(img, mode='pepper',amount=amountrange)
    noise_img = np.array(255*noise_img, dtype = 'uint8')
    return noise_img

# import torch
# import cv2
# import numpy as np
# from skimage.util import random_noise

# def pepper(imagelocation):
#     amountrange = 0.3
#     img = cv2.imread(imagelocation)
#     img_tensor = torch.from_numpy(np.transpose(img, (2, 0, 1)))
#     img_tensor = img_tensor.unsqueeze(0)
#     img_tensor = img_tensor.float() / 255.0

#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#     img_tensor = img_tensor.to(device)

#     noise_img = random_noise(img_tensor.cpu().numpy()[0], mode='pepper', amount=amountrange)
#     noise_img = np.array(255*noise_img, dtype='uint8')

#     return noise_img




# import cv2
# import numpy as np
# from skimage.util import random_noise

# try:
#     import cupy as cp
#     USE_GPU = True
# except ImportError:
#     USE_GPU = False

# def pepper(imagelocation):
#     amountrange = 0.3
#     img = cv2.imread(imagelocation)
#     if USE_GPU:
#         img = cp.asarray(img)
#     noise_img = random_noise(img, mode='pepper', amount=amountrange)
#     if USE_GPU:
#         noise_img = cp.asnumpy(noise_img)
#     noise_img = np.array(255*noise_img, dtype='uint8')
#     return noise_img


# import numpy as np
# from skimage.util import random_noise

# def pepper(imagelocation):
#     amountrange = 0.3
#     img = cv2.imread(imagelocation)
#     noise_img = random_noise(img, mode='pepper', amount=amountrange)
#     noise_img = np.array(255*noise_img, dtype='uint8')
#     return noise_img


# peppernoise(r"C:\Users\fredd\Documents\GitHub\Prism-gui-image-augment\images\image-25.jpg",0.3)