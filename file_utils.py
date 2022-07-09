import os
from pathlib import Path


def list_image_files(directory):
    image_files = []
    for entry in os.scandir(directory):
        if entry.is_file() and is_image_file(entry.name):
            image_files.append(entry.path)
    return image_files


def is_image_file(file):
    extension = Path(file).suffix
    if extension in [".jpeg", ".jpg", ".png"]:
        return True
    else:
        return False
