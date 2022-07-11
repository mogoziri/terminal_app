from image_processing import grayscale, rotate, resize
from file_utils import list_image_files, is_image_file
import argparse

# grayscale("./test/picture_1.jpeg")
#
# rotate("./test/picture_1.jpeg")
#
resize("./test/picture_1.jpeg")


#
# is_image_file("./test/picture_1.jpeg")
# print(is_image_file("./test/picture_1.txt"))

parser = argparse.ArgumentParser(description="Photo Processor")
parser.add_argument("--directory", required=True)
parser.add_argument("--operation", choices=["grayscale", "rotate", "resize"], nargs="+", required=True)
args = parser.parse_args()

image_files = list_image_files(args.directory)
print(image_files)

