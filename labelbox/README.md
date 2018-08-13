
#Labelbox WKT JSON export to KITTI format

1. All image data should pooled into a parent directory on the host computer
2. Download a Well-known Text JSON export of your labelbox project after all of the images have been annotated.
3. clone and install the [labelbox2coco api](https://github.com/Labelbox/Labelbox/tree/master/scripts). Follow the README.md instructions in the labelbox scripts folder. You can use the json2coco.py script in the ./script folder of this directory if desired, or make your own.
4. Run the script and retrieve the coco.json output file.
5. clone the [python COCO api](https://github.com/cocodataset/cocoapi), using the same, or a separate python environment. Add the COCO api directory to your pythonpath (**.bashrc >> 'export PYTHONPATH="${PYTHONPATH}:/home/user/bin/cocoapi/PythonAPI"'**)
6. Download the coco2kitti.py script provided in the [Jetson-Inference Project](https://github.com/dusty-nv/jetson-inference/blob/master/tools/coco2kitti.py)
7. Run the script changing the *annFile* variable to the location of your coco.json file.
8. You should now have a folder with your annotated data in the form of individual text files.
9. The next step is to organize the image and the label text data into the KITTI file format:
```
train/
├── images/
│   └── 000001.png
└── labels/
    └── 000001.txt
val/
├── images/
│   └── 000002.png
└── labels/
    └── 000002.txt
```
10. Use *kitti_struct.py* script found in the ./scripts folder of this directory. Change the input and output directory locations of your data following the instructions in the script and run the script.
    - NOTE: the train validation data split is set to 15%, either take out the test_size argument, or change to 0.25.
11. data should now be formatted correctly for use with DIGITS.
