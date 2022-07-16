import os
from pathlib import Path


def list_image_files(directory):
    """
    Lists all images in a directory

    Arguments:
        directory : specifies path that should be scanned for image files

    Returns:
        list of image files from specified directory
    """
    image_files = []
    for entry in os.scandir(directory):
        if entry.is_file() and is_image_file(entry.name):
            image_files.append(entry.path)
    return image_files


def is_image_file(file):
    """
    Checks if specified file is an image

    Arguments:
        file: file in a directory

    Returns:
        True if specified file is an image file with extensions .jpeg, .jpg, .png
        False otherwise
    """
    extension = Path(file).suffix
    if extension in [".jpeg", ".jpg", ".png"]:
        return True
    else:
        return False


def create_destination_path(source_path, destination_path):
    """
    Creates a file in destination directory with same name as source file

    Arguments:
        source_path : path to a source file
        destination_path : destination directory

    Returns:
        Path object corresponding to file in destination directory
    """
    source_name = Path(source_path).name
    return Path(destination_path, source_name)
