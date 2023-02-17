# Import Image from wand.image module
from wand.image import Image
  
# Read image using Image() function
def uniformnoise(imagelocation,attenuaterange):
    with Image(filename = imagelocation) as img:
        img.noise("random", attenuate = attenuaterange)
        # img.save(filename ="random.jpeg")

uniformnoise(r"C:\Users\fredd\Documents\GitHub\Prism-gui-image-augment\images\image-28.jpg",0.9)