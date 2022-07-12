# Importing Image and ImageOps module from PIL package
from PIL import ImageOps


def grayscale(image):
    # applying grayscale method
    gray_image = ImageOps.grayscale(image)
    return gray_image


def rotate(image):
    # applying rotation method
    rotated_image = image.rotate(90)
    return rotated_image


def resize(image):
    w, h = image.size
    bounding_box = (int(w/2), int(h/2))
    # applying resizing method
    resized_image = ImageOps.fit(image, bounding_box)
    return resized_image
