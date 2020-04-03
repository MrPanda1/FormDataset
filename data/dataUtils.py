"""
Utility functions related to manipulating and fetching the data
"""
import os
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image

# Gets "annotation" and "images" subfolders from a directory
def get_dir_paths(dir):
    imgDir = ""
    annotationDir = ""
    for item in os.scandir(dir):
        if item.name.startswith("images") and item.is_dir():
            imgDir = os.path.join(dir, item.name)
        if item.name.startswith("annotations") and item.is_dir():
            annotationDir = os.path.join(dir, item.name)
    
    return imgDir, annotationDir

def get_images(dir):
    imgs = []
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        im = Image.open(os.path.join(dir, filename))
        imgs.append(im)
        
    return imgs
    
def get_annotation(root):
    annotation = { "name": "", "size": [], "bndboxes": [] }
    for child in root:
        if child.tag == "filename":
            annotation["name"] = child.text
        if child.tag == "size":
            annotation["size"] = [int(dim.text) for dim in child]
        if child.tag == "object":
            bndbox = child.find("bndbox")
            x_coords = [int(bndbox[0].text), int(bndbox[2].text)]
            y_coords = [int(bndbox[1].text), int(bndbox[3].text)]
            
            label = child.find("name")
            
            bndbox_info = { "label": label.text, 
                            "coords": [x_coords, y_coords] }
            annotation["bndboxes"].append(bndbox_info)
    
    return annotation
    
def get_annotations(dir):
    annotations = []

    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        tree = ET.parse(os.path.join(dir, filename))
        root = tree.getroot()
        
        annotation = get_annotation(root)
        annotations.append(annotation)

    return annotations
    
def bndbox_size(coords):
    size = np.array([dim[1]-dim[0] for dim in coords])
    return size
    
def downscale_img(img, max_dim):
    width, height = img.size
    
    ratio = max_dim/max(width, height)
    new_size = (int(round(width*ratio)), int(round(height*ratio))) 
    img = img.resize(new_size)
    
    return img

"""
Description: Calculates the ratio of bounding box area to image area.
             Call this the "BBI Ratio" for short.
Input: Bounding box coordinates and image size
Output: Ratio between bounding box area and image area
"""
def bbi_ratio(bndbox_coords, img_size):
    bndbox_area = np.prod(bndbox_size(bndbox_coords))
    img_area = img_size[0] * img_size[1]
    
    return bndbox_area / img_area
    
"""    
Description: Separates raw data into an array of labels and an 
             array of data where they correspond to each other by 
             index.              
Input: Dictionary of annotations
Output: Tuple of numpy array containing labels and numpy array
        containing a numpy array of the bounding box coordinates
"""
def split_data_and_labels(raw_data):
    labels = []
    data = []
    
    for annotation in raw_data:
        for bndbox in annotation["bndboxes"]:
            data.append(bndbox)
            labels.append(bndbox["label"])
    
    return np.array(data), np.array(labels)

"""    
Description: Separates data (in this case bounding boxes) by their 
             label/class
Input: Numpy array of data, Numpy array of labels
Output: Dictionary of data split by labels
"""
def split_by_class(data, labels):
    classes = {}
    for sample in range(data.shape[0]):
        if labels[sample] not in classes.keys():
            classes[labels[sample]] = [data[sample]]
        else:
            classes[labels[sample]].append(data[sample])
    return classes
    