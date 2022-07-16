## T1A3 Terminal Application "Photo Processor"

### A link to source control repository
Link to GitHub 
https://github.com/mogoziri/terminal_app

### Photo Processor overview
The photo processor application allows user to perform basic photo editing operations. Users indicate a source directory containing images which need to be processed and a destination directory where edited photos will be saved. If destination directory doesn't exist application will create it. The application processes all the images in the folder in one run. Users can apply several operations at the same time.


### List of Application Features

- Argparse feature - binds command line arguments to Python variables
- Grayscale feature - transforms an image to black and white variant
- Rotate feature - rotates an image to 90 degrees
- Resize feature - resizes an image 2 times smaller keeping the aspect ratio
- Blur feature - applies a blurring effect on to the image

- Flip feature - flips an image horizontally
- Contour feature - applies contour effect on to the image
- Invert feature - inverts pixel values of the image
- Detail feature - applies detail effect on to the image
- Sharpen feature - applies sharpen effect on to the image

### Implementation Plan
The implementation plan was created using a Trello Board in a web-based list-making application developed by Trello Enterprise.

Photo Processor implementation plan (main board):

### Style Guide
PEP8 Style Guide for Python Code

Shell script `format.sh` used to run `autopep8` utility on all python source files.

### Help Documentation

Steps to install and run the application:  
1.  Run `pip install -r requirements.txt`  in your terminal to install third-party dependencies
2.  Run `python3 main.py`

Any dependencies required by the application to operate:

 1. Python 3
 2. Pip

System/hardware requirements:  

 1. Unix-like operating system (Linux / MacOS)

Command line arguments description:
- source directory - directory contains image files which user wants to transform
- destination directory - processed files will be saved into this directory
- operation: grayscale, rotate, resize, blur, flip, contour, invert, detail, sharpen

### Testing
**Test #1 scenario** 

Run application with no parameters and it returns an error with required arguments description. 
Next time, specify all arguments such as source directory, destination directory and required operations (rotation and grayscale effect). This time test runs correctly.

**Test #2 scenario**

Run application with missing arguments to check error handling.

- First case, specify a non-existent operation `bright`.
- Second case, missing a source directory argument.
- Third case, missing a destination directory argument.

In all cases it returns an error requesting missing parameters.

### Reference List
van Rossum, G., Warsaw, B. and Coghlan, N. (2001). _Style Guide for Python Code_. [online] GitHub. Available at: https://github.com/python/peps/blob/main/pep-0008.txt [Accessed 10 Jul. 2022].
