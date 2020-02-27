import os

# Change working directory to be inside the images folder
os.chdir("./downscaled/annotations/")

array = []
for i in range(500):
        array.append(False)

# Get every image in the directory
for file in os.listdir(os.getcwd()):
    filename = os.fsdecode(file)
    splitFilename = filename.split(".", 1)
    array[int(splitFilename[0])-1] = True

# Print result
for index, boolean in enumerate(array):
        if not boolean:
                print(index+1)