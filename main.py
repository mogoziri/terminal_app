from image_processing import grayscale, rotate, resize
from file_utils import list_image_files, is_image_file, create_destination_path
import argparse
from pathlib import Path


# grayscale("./test/picture_1.jpeg")
#
# rotate("./test/picture_1.jpeg")
#
# resize("./test/picture_1.jpeg")


#
# is_image_file("./test/picture_1.jpeg")
# print(is_image_file("./test/picture_1.txt"))

parser = argparse.ArgumentParser(description="Photo Processor")
parser.add_argument("--source_directory", required=True)
parser.add_argument("--destination_directory", required=True)
parser.add_argument("--operation", choices=["grayscale", "rotate", "resize"], nargs="+", required=True)
args = parser.parse_args()

image_files = list_image_files(args.source_directory)
print(image_files)

Path(args.destination_directory).mkdir()

for image in image_files:
    transformed_image = grayscale(image)
    destination_path = create_destination_path(image, args.destination_directory)
    print(destination_path)
    transformed_image.save(destination_path)
