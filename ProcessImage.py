from PIL import Image
from numpy import asarray


image = Image.open("Cube.png")

# convert image to numpy array
data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)
