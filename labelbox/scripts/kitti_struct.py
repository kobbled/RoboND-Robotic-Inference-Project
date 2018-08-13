#!/usr/bin/env python

# # kitti_struct.py
# # Author: Matt Dewar
# # Date: Aug8, 2018
# # Description: This script take a file dump of images and KITTI formatted
# #              text labels and sorts them into the a KITTI folder structure
# # train/
# # ├── images/
# # │   └── 000001.png
# # └── labels/
# #     └── 000001.txt
# # val/
# # ├── images/
# # │   └── 000002.png
# # └── labels/
# #     └── 000002.txt
# # ref : https://github.com/NVIDIA/DIGITS/blob/digits-4.0/digits/extensions/data/objectDetection/README.md
# #
# # IMAGE_DIR, and LABEL_DIR point to the directories of the images, and txt labels respectively
# # TRAIN_SAV, and VAL_SAV are the directories to save the training and validation data
# # train_pickle, and val_pickle are the files to save dictionary elements of the training and validation data
# # dictionary elements are formatted such as:
# #             filename : {label: fildir/to/label, image: fildir/to/image}
# ---
# ---

import os
import glob
import pickle
from sklearn.model_selection import train_test_split
from shutil import copyfile


def create_dict(labels, img_dir):
    file_dict = {}
    for file in labels:
        file_name = os.path.splitext(file)[0].rsplit('/', 1)[1]
        image = glob.glob(img_dir + '/**/' + file_name + '.png', recursive=True)
        file_dict[file_name] = {'label': file, 'image': image}
    return file_dict


def make_pickle(filename, data):
    if not os.path.isfile(filename):
        outfile = open(filename, 'wb')
        pickle.dump(data, outfile)
        outfile.close()


def format2KITTI(dict, fldir):
    for key in dict:
        # print(dict[key])
        copyfile(dict[key]['image'][0], fldir + 'images/' + key + '.png')
        copyfile(dict[key]['label'], fldir + 'labels/' + key + '.txt')


if __name__ == "__main__":
    IMAGE_DIR = "./classification-data/images/"
    LABEL_DIR = "./classification-data/labels/"
    TRAIN_SAV = "./data/train/"
    VAL_SAV = "./data/val/"
    train_pickle = 'train.pickle'
    val_pickle = 'val.pickle'

    if not os.path.isfile(train_pickle):
        # get list of label Files
        label_files = glob.glob(os.path.join(LABEL_DIR, "*.txt"))
        # Split data into training, and validation lists
        label_train, label_val = train_test_split(label_files, test_size=0.15, random_state=42)

        # create dictionary for training set
        train_dict = create_dict(label_train, IMAGE_DIR)
        # save to pickle
        make_pickle(train_pickle, train_dict)
        # create dictionary for validation set
        val_dict = create_dict(label_val, IMAGE_DIR)
        # save to pickle
        make_pickle('val.pickle', val_dict)
    else:
        # load training dict
        infile = open(train_pickle, 'rb')
        train_dict = pickle.load(infile)
        # print(train_dict)
        infile.close()
        # load val dict
        infile = open(val_pickle, 'rb')
        val_dict = pickle.load(infile)
        # print(val_dict)
        infile.close()

    # copy files to respective location
    format2KITTI(train_dict, TRAIN_SAV)
    format2KITTI(val_dict, VAL_SAV)
