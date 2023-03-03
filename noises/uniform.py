# Import Image from wand.image module
from wand.image import Image
  
# Read image using Image() function
def uniformnoise(imagelocation):
    attenuaterange = 0.9
    with Image(filename = imagelocation) as img:
        img.noise("uniform", attenuate = attenuaterange)
        # img.save(filename ="uniformnoise.jpeg")
    return img

# uniformnoise(r"C:\Users\fredd\Documents\GitHub\Prism-gui-image-augment\images\image-28.jpg",0.9)