#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from PIL import Image
import os

base_directory = os.path.dirname(os.path.realpath(__file__))

directory_in_str = base_directory + '/annotations'

directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    tree = ET.parse('./annotations/' + filename)
    root = tree.getroot()

    if(root[4][0].text == '0' or root[4][1] == '0'):
        print("------------------------ IMAGE = " + filename + " ------------------------")
        print("-----\t\tOriginal\t-----")
        print("Width: " + root[4][0].text)
        print("Height: " + root[4][1].text)

        image_filename = base_directory + '/images/' + filename[:-4] + '.png'
            
        im = Image.open(image_filename)
        width, height = im.size

        print("-----\t\tActual\t\t-----")
        print("Width: " + str(width))
        print("Height: " + str(height))

        root[4][0].text = str(width)
        root[4][1].text = str(height)
        tree.write('./annotations/' + filename)
        print("Updated XML")