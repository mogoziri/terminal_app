from image_processing import grayscale, rotate, resize
from file_utils import list_image_files, is_image_file, create_destination_path
import argparse
from pathlib import Path
from PIL import Image


parser = argparse.ArgumentParser(description="Photo Processor")
parser.add_argument("--source_directory", required=True)
parser.add_argument("--destination_directory", required=True)
parser.add_argument("--operation", choices=["grayscale", "rotate", "resize"], nargs="+", required=True)
args = parser.parse_args()

image_files = list_image_files(args.source_directory)
print(image_files)

Path(args.destination_directory).mkdir(exist_ok=True)

for image_file in image_files:
    image = Image.open(image_file)
    transformed_image = grayscale(image)
    destination_path = create_destination_path(image_file, args.destination_directory)
    print(destination_path)
    transformed_image.save(destination_path)
