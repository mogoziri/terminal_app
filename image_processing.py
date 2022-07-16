from PIL import ImageOps, ImageFilter, Image


def grayscale(image):
    """
    Applies grayscale method

    Arguments:
        image : source image file

    Returns:
         transformed image into black and white variant
    """
    gray_image = ImageOps.grayscale(image)
    return gray_image


def rotate(image):
    """
    Applies rotation method

    Arguments:
        image: source image file

    Returns:
        rotated image to 90 degrees counterclockwise
    """
    rotated_image = image.rotate(90)
    return rotated_image


def resize(image):
    w, h = image.size
    bounding_box = (int(w / 2), int(h / 2))
    """
    Applies resize method

    Arguments:
        image : source image file

    Returns:
        resized image 2 times smaller keeping the aspect ratio
    """
    resized_image = ImageOps.fit(image, bounding_box)
    return resized_image


def blur(image):
    """
    Applies blur method

    Arguments:
        image : source image file

    Returns:
        blurred image
    """
    blur_image = image.filter(ImageFilter.BLUR)
    return blur_image


def flip(image):
    """
    Applies flip method

    Arguments:
        image : source image file

    Returns:
         flipped image horizontally
    """
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_image


def contour(image):
    """
    Applies contour method

    Arguments:
        image : source image file

    Returns:
        image with contour effect
    """
    contour_image = image.filter(ImageFilter.CONTOUR)
    return contour_image


def invert(image):
    """
    Applies invert method

    Arguments:
        image : source image file

    Returns:
        inverted image
    """
    inverted_image = ImageOps.invert(image)
    return inverted_image


def detail(image):
    """
    Applies detail method

    Arguments:
        image : source image file

    Returns:
        image with detail effect
    """
    detailed_image = image.filter(ImageFilter.DETAIL)
    return detailed_image


def sharpen(image):
    """
    Applies sharpen method

    Arguments:
        image : source image file

    Returns:
        image with sharpen effect
    """
    sharpened_image = image.filter(ImageFilter.SHARPEN)
    return sharpened_image


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
    elif op == "sharpen":
        return sharpen(image)
    else:
        print("unknown operation")
