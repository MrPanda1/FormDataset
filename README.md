# FormDataset
Repository contains images of forms and their respective annotations in PASCAL VOC format (XML Files).

## Contributing
All images are stored in [data/images](https://github.com/MrPanda1/FormDataset/blob/master/data/images) and all annotations are saves in [data/annotations](https://github.com/MrPanda1/FormDataset/blob/master/data/annotations). Please look at [CONTRIBUTORS](https://github.com/MrPanda1/FormDataset/blob/master/CONTRIBUTORS.md) to see who is responsible for what images. Make sure to save all images with the numbers assigned to you and to save all images and annotations in the correct folders. All annotations should be in XML PASCAL VOC format.

## Installation

### Build from source
[Python 3 or above](https://www.python.org/getit/) and
[PyQt5](https://pypi.org/project/PyQt5/) are strongly recommended.

#### macOS
*Python 3 Virtualenv*

Virtualenv can avoid a lot of the QT / Python version issues

``` shell
brew install python3
pip3 install pipenv
pipenv --three # or pipenv install pyqt5 lxml
pipenv run pip install pyqt5 lxml
pipenv run make qt5py3
python3 labelImg.py
```

#### Windows
Install [Python](https://www.python.org/downloads/windows/),
[PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5) and
\`install lxml \<<http://lxml.de/inst>

Open cmd and go to the [labelImg](#labelimg) directory

``` shell
pyrcc4 -o line/resources.py resources.qrc
For pyqt5, pyrcc5 -o libs/resources.py resources.qrc

python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

#### Windows + Anaconda

Download and install
[Anaconda](https://www.anaconda.com/download/#download) (Python 3+)

Open the Anaconda Prompt and go to the [labelImg](#labelimg) directory

``` shell
conda install pyqt=5
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

### Usage Steps (PascalVOC)

1.  Build and launch using the instructions above.
2.  Click 'Change default saved annotation folder' in Menu/File
3.  Click 'Open Dir'
4.  Click 'Create RectBox'
5.  Click and release left mouse to select a region to annotate the rect
    box
6.  You can use right mouse to drag the rect box to copy or move it

The annotation will be saved to the folder you specify.

You can refer to the below hotkeys to speed up your workflow.

## Hotkeys

|          |                                           |
| -------- | ----------------------------------------- |
| Ctrl + u | Load all of the images from a directory   |
| Ctrl + r | Change the default annotation target dir  |
| Ctrl + s | Save                                      |
| Ctrl + d | Copy the current label and rect box       |
| Space    | Flag the current image as verified        |
| w        | Create a rect box                         |
| d        | Next image                                |
| a        | Previous image                            |
| del      | Delete the selected rect box              |
| Ctrl++   | Zoom in                                   |
| Ctrl--   | Zoom out                                  |
| ↑→↓←     | Keyboard arrows to move selected rect box |

**Verify Image:**

When pressing space, the user can flag the image as verified, a green
background will appear. This is used when creating a dataset
automatically, the user can then through all the pictures and flag them
instead of annotate them.

**Difficult:**

The difficult field is set to 1 indicates that the object has been
annotated as "difficult", for example, an object which is clearly
visible but difficult to recognize without substantial use of context.
According to your deep neural network implementation, you can include or
exclude difficult objects during training.

## License

[Free software: MIT
license](https://github.com/MrPanda1/FormDataset/blob/master/LICENSE)

## Credits
Using [labelImg by tzutalin](https://github.com/tzutalin/labelImg)
Citation: Tzutalin. LabelImg. Git code (2015).
<https://github.com/tzutalin/labelImg>