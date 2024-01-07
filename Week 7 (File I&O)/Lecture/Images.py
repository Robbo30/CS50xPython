import sys 
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

image[0].save(
    "costume.gif", saveAll=True, appendImages=[images[1]], duration=200, loop=0
)