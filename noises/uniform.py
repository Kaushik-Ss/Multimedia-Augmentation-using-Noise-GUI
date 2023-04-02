# from wand.image import Image
  
# def uniformnoise(imagelocation):
#     attenuaterange = 0.9
#     with Image(filename = imagelocation) as img:
#         img.noise("uniform", attenuate = attenuaterange)
#         # img.save(filename ="uniformnoise.jpeg")
#     return img

# # uniformnoise(r"C:\Users\fredd\Documents\GitHub\Prism-gui-image-augment\images\image-28.jpg",0.9)

import cv2
import numpy as np
import torch

def uniform(imagelocation):
    img = cv2.imread(imagelocation, 0)
    intensity = 0.1
    noise = np.random.uniform(-intensity, intensity, img.shape)
    noisy_img = img + noise.astype(np.uint8)

    # check if a GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # move the image and noise tensors to the device
    img_tensor = torch.tensor(noisy_img).to(device)
    noise_tensor = torch.tensor(noise.astype(np.uint8)).to(device)
    
    # perform the addition operation on the GPU
    noisy_img_gpu = torch.add(img_tensor, noise_tensor).cpu().numpy()

    return noisy_img_gpu
