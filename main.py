from image_processing import grayscale, rotate, resize
from file_utils import list_image_files, is_image_file
import argparse

# grayscale("./test/picture_1.jpeg")
#
# rotate("./test/picture_1.jpeg")
#
# resize("./test/picture_1.jpeg", (500, 500))

# list_image_files("./test")
# print(list_image_files("./test"))
#
# is_image_file("./test/picture_1.jpeg")
# print(is_image_file("./test/picture_1.txt"))

parser = argparse.ArgumentParser(description="Photo Processor")
parser.add_argument("--directory", help="directory help")
args = parser.parse_args()
print(args)

