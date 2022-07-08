# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps


def grayscale(path_to_file):
    # creating an og_image object
    og_image = Image.open(path_to_file)

    # applying grayscale method
    gray_image = ImageOps.grayscale(og_image)
    gray_image.show()

def rotate(path_to_file):
    # creating an og_image object
    og_image = Image.open(path_to_file)

    # applying rotation method
    rotated_image = og_image.rotate(90)
    rotated_image.show()