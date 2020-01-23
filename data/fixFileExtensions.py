import imghdr
import os
from PIL import Image

# Change working directory to be inside the images folder
os.chdir("./images/")

# Get every image in the directory
for file in os.listdir(os.getcwd()):
    filename = os.fsdecode(file)
    imageType = imghdr.what(filename)
    splitFilename = filename.split(".", 1)
    imageExtension = splitFilename[1]

    # Fix if image type is not a png or image extension is not "png"
    if (imageType != "png" or imageExtension != "png"):
        print("BEFORE: " + filename + "\t" + imageType)
        
        image = Image.open(filename)
        filenameNoExt = splitFilename[0]
        correctFilename = filenameNoExt + ".png"
        image.save(correctFilename)

        correctImageType = imghdr.what(correctFilename)
        print("AFTER: " + correctFilename + "\t" + correctImageType)
