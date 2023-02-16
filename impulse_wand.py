# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='pic1.jpg') as image:
	# Clone the image in order to process
	with image.clone() as noise:
		# Invoke noise function with Channel "green" and noise poisson
		noise.noise("impulse", 2, "green")
		# Save the image
		noise.save(filename ='noise1.jpg')
