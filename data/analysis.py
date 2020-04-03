import os
import math
import dataUtils as dut
import numpy as np
import matplotlib.pyplot as plt

"""
Description: Plots data as a histogram to see the distribution.
             Additionally prints out mean and standard deviation.
Input: Numpy array of data
Output: None
"""
def plot_distrib(data, num_bins=0, title="", xlabel=""):
    # If number of bins not specified, use this one
    if num_bins == 0:
        num_bins = math.ceil(math.sqrt(data.shape[0]))
    
    # Plot histogram
    plt.hist(data, num_bins)
    
    # Plot settings
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    
    plt.show()

def main():
    # Get the data directories
    homeDir = os.getcwd()
    dataDir = os.path.join(homeDir, "original")
    imgDir, annotationDir = dut.get_dir_paths(dataDir)
    
    # Extract images and their respective annotations from directories
    imgs = dut.get_images(imgDir)
    annotations = dut.get_annotations(annotationDir)
    
    # Get image sizes
    img_sizes = np.array([a["size"] for a in annotations])
    
    # Split bounding boxes into labels and data
    bb_data, bb_labels = dut.split_data_and_labels(annotations)
    
    # Generate BBI ratio data from annotations
    bbi_data = []
    bb_index = 0;
    for annotation in annotations:
        num_bndboxes = len(annotation["bndboxes"])
        img_size = annotation["size"]
        
        annotation_bbis = [dut.bbi_ratio(bb_data[i + bb_index]["coords"], img_size) for i in range(num_bndboxes)]
        
        bbi_data += annotation_bbis
        bb_index += num_bndboxes

    bbi_data = np.array(bbi_data)

    # Split data further by classes
    bbi_class_data = dut.split_by_class(bbi_data, bb_labels)
    
    # Plot BBI ratio distributions
    plot_distrib(bbi_data, title="Total BBI Ratio Distribution", xlabel="BBI Ratio")
    
    for label in bbi_class_data.keys():
        plot_title = "{} BBI Ratio Distribution".format(label)
        plot_distrib(np.array(bbi_class_data[label]), title=plot_title, xlabel="BBI Ratio")
        
    # Plot class counts
    plot_distrib(bb_labels, num_bins=5, title="Total Class Counts", xlabel="Classes")
    
    # Plot image sizes/areas
    img_areas = np.array([img[0] * img[1] for img in img_sizes])
    x_dim_avg = round(np.mean([img[0] for img in img_sizes]))
    y_dim_avg = round(np.mean([img[1] for img in img_sizes]))
    plot_distrib(img_areas, title="Image Area Distribution", xlabel="Areas")
    print("Average image area: {}".format(round(np.mean(img_areas))))
    print("Average image dimensions: ({}, {})".format(x_dim_avg, y_dim_avg))

    # TODO figure out a thing to do this
    # Calculate (possibly) optimal image downscale size
    for img in imgs:
        grayscale_img = img.convert("L")
        full_avg = np.mean(np.array(grayscale_img))
        
        downscaled_img = dut.downscale_img(grayscale_img, 100)
        downscaled_avg = np.mean(np.array(downscaled_img))
        
        print("Full size: {}\nDownscaled size: {}".format(full_avg, downscaled_avg))
        
        break

if __name__ == "__main__":
    main()
