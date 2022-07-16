from image_processing import apply_transformation
from file_utils import list_image_files, create_destination_path
import argparse
from pathlib import Path
from PIL import Image


parser = argparse.ArgumentParser(description="Photo Processor")
parser.add_argument("--source_directory", required=True)
parser.add_argument("--destination_directory", required=True)
parser.add_argument("--operation", choices=["grayscale", "rotate", "resize", "blur", "flip", "contour", "invert", "detail", "sharpen"], nargs="+", required=True)
args = parser.parse_args()

image_files = list_image_files(args.source_directory)

# creating new destination folder, not fail if already exists
Path(args.destination_directory).mkdir(exist_ok=True)

for image_file in image_files:
    image = Image.open(image_file)
    for op in args.operation:
        image = apply_transformation(image, op)
    destination_path = create_destination_path(image_file, args.destination_directory)
    image.save(destination_path)
