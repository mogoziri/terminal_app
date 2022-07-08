# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

# creating an og_image object
og_image = Image.open("./test/picture_1.jpeg")
og_image.show()

# applying grayscale method
gray_image = ImageOps.grayscale(og_image)
gray_image.show()
