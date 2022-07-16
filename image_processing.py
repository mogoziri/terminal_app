# Importing Image and ImageOps module from PIL package
from PIL import ImageOps, ImageFilter, Image


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


def blur(image):
    # applying blur method
    blur_image = image.filter(ImageFilter.BLUR)
    return blur_image


def flip(image):
    # applying flip method
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_image


def contour(image):
    # applying contour method
    contour_image = image.filter(ImageFilter.CONTOUR)
    return contour_image


def invert(image):
    # applying invert method
    inverted_image = ImageOps.invert(image)
    return inverted_image


def detail(image):
    # applying contour method
    detailed_image = image.filter(ImageFilter.DETAIL)
    return detailed_image


def apply_transformation(image, op):
    if op == "grayscale":
        return grayscale(image)
    elif op == "rotate":
        return rotate(image)
    elif op == "resize":
        return resize(image)
    elif op == "blur":
        return blur(image)
    elif op == "flip":
        return flip(image)
    elif op == "contour":
        return contour(image)
    elif op == "invert":
        return invert(image)
    elif op == "detail":
        return detail(image)
    else:
        print("unknown operation")
