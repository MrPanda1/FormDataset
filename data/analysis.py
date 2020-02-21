import os
import math
import dataUtils as dut
import numpy as np
import matplotlib.pyplot as plt

"""
Description: Plots data as a histogram to see the distribution.
             Additionally prints out mean and standard deviation.
Input: Numpy array of data
Output: Mean and standard deviation of the data
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
    
    return np.mean(data, axis=0), np.std(data, axis=0)

def main():
    # Get the data directories
    homeDir = os.getcwd()
    dataDir = os.path.join(homeDir, "original")
    imgDir, annotationDir = dut.get_dir_paths(dataDir)
    
    # Extract images and their respective annotations from directories
    imgs = dut.get_images(imgDir)
    annotations = dut.get_annotations(annotationDir)
    
    # Split bounding boxes into labels and data
    data, labels = dut.split_data_and_labels(annotations)
    
    # Split data further by classes
    class_data = dut.split_by_class(data, labels)
    
    plot_distrib(data, title="Total BBI Ratio Distribution", xlabel="BBI Ratio")
    
    for label in class_data.keys():
        plot_title = "{} BBI Ratio Distribution".format(label)
        plot_distrib(np.array(class_data[label]), title=plot_title, xlabel="BBI Ratio")

if __name__ == "__main__":
    main()