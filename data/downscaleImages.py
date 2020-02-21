import os
import xml.etree.ElementTree as ET
from PIL import Image

# Save current directory to reset later
homeDir = os.getcwd()

# Change working directory to be inside the images folder
os.chdir("./downscaled/images/")

# Max Image Dimension = 416 x 416
maxDimension = 416

# Get every image in the directory
for file in os.listdir(os.getcwd()):
    print(file)
    filename = os.fsdecode(file)

    im = Image.open(filename)
    width, height = im.size
    
    ratio = maxDimension/max(width, height)
    newSize = (int(round(width*ratio)), int(round(height*ratio))) 
    im = im.resize(newSize)
    # Save image
    im.save(filename, "png")

    im = Image.open(filename)
    afterWidth, afterHeight = im.size
    print("----- IMAGE {} -----\n \
            Before: W: {}\tH: {}\n \
            After: W: {}\tH: {}".format(filename, width, height, afterWidth, afterHeight))

# Change working directory to be inside the annotations folder
os.chdir(homeDir + "/downscaled/annotations/")

# Get dimension from every XML in the directory
for file in os.listdir(os.getcwd()):
    filename = os.fsdecode(file)
    tree = ET.parse(filename)
    root = tree.getroot()

    # Height and Width from XML file
    width = int(root[4][0].text)
    height = int(root[4][1].text)

    # Ratio to be multiplied by all other numbers
    ratio = maxDimension/max(width, height)

    # Fix the height and width in XML
    newWidth = int(round(width*ratio))
    newHeight = int(round(height*ratio))
    root[4][0].text = str(newWidth)
    root[4][1].text = str(newHeight)


    for child in root:
        if child.tag == "object":
            bndbox = child.find("bndbox")
            # xmin = bndbox.find("xmin")
            # print(xmin.text)
            for coord in bndbox:
                coord.text = str(round(int(coord.text)*ratio))

    # Save changes
    tree.write(filename)