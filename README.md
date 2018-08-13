# RoboND - Robotic Inference Project

This repository is for the Udacity RoboND Robotic Inference Project, classifying and detecting real world objects leveraging the NVIDIA DIGITS workflow for efficient experimentation with Deep learning networks such as AlexNet, GoogLeNet, and the DetectNet Architecture.

The first dataset involves the classification of two objects on a conveyor belt, as well as 'None' state. An example of the dataset is shown in Figure 1.

|![alt text][sample_data]|
|:----:|
|**Figure 1 : Sample dataset of Udacity supplied conveyor data**|

Images for this data structure were organized like that shown below in order to successfully import the data into a DIGITS classification dataset.

```
P1_data/
├── Bottle/
│   ├── Bottle_1.png
│   └── Bottle_2.png
├── Candy_box/
│   ├── Candy_box_1.png
│   └── Candy_box_2.png
└── Nothing/
    ├── Nothing_1.png
    └── Nothing_2.png
```

Evaluation of the dataset trained on a GoogLeNet network for 10 Epochs revealed an accuracy of 75.4%, and an inference time of ~5.3 ms.

|![P1 model evaluation][sample_evaluate]|
|:----:|
|**Figure 2 : Evaluation of the GoogLeNet network on the conveyor products dataset**|

The trained model can be found in *./DIGITS/P1-Test_Dataset* of this repository.

The model trained with the conveyor belt test data was then applied to collected data from UniFi video cameras monitoring a workcell at a welding fabrication facility involving people and a robot.

Classification data was broken down as:

```
Workcell1/
├── Person/
│   ├── person00001.png
│   └── person00002.png
├── Person-Robot/
│   ├── person-robot00001.png
│   └── person-robot00002.png
└── Robot/
|    ├── robot00001.png
|    └── robot00002.png
└── None/
    ├── none00001.png
    └── none00002.png
```

Examples of the training data are shown in Figure 3.
|![WC1 training data][WC1-data]|
|:----:|
|**Figure 3 : training data for workcell 1**|

The trained model for the above classification can be found in *./DIGITS/Workcell1-Classification/GoogLeNet-initial* of this repository.  

Figure 4 shows the loss and accuracy tensorboard plots of the training and validation data respectively.

|![WC1 model evaluation][WC1-loss-accuracy]|
|:----:|
|**Figure 4 : Loss and accuracy of training and validation data over 10 epochs using GoogLeNet**|

This model was further improved by training for another 12 Epochs using the initial GoogLeNet model as the pretrained network.

|![WC1 model evaluation][WC1-loss-accuray2]|
|:----:|
|**Figure 5 : Loss and accuracy of training and validation data over 12 epochs using the pretrained model above.**|

Lastly object detection was attempted on monitor cameras from another workcell, using the [Labelbox](https://labelbox.com/) platform for image annotation.

|![Image Annotation][WC2-image-annotation]|
|:----:|
|**Figure 6 : Image annotation for workcell 2 using Labelbox**|

Image and annotation data was structured into the KITTI format (see *./labelbox/scripts*):

```
train/
├── images/
│   └── Robot00001.png
│   └── Person00001.png
│   └── Person-Robot00001.png
└── labels/
    └── Robot00001.txt
    └── Person00001.txt
    └── Person-Robot00001.txt
val/
├── images/
│   └── Robot00002.png
│   └── Person00002.png
│   └── Person-Robot00002.png
└── labels/
    └── Robot00002.txt
    └── Person00002.txt
    └── Person-Robot00002.txt
```

Following the [example guide](https://devblogs.nvidia.com/deep-learning-object-detection-digits/), the  [detectnet.prototxt](https://github.com/dusty-nv/jetson-inference/blob/master/data/networks/detectnet.prototxt) network was used for training and validation with a [pretrained GoogLeNet model](https://github.com/BVLC/caffe/tree/rc3/models/bvlc_googlenet). The trained model snapshot can be found in *./DIGITS/Workcell2-Object_detection/model* of this repository. The loss and accuracy tensorboard, Figure 7, show that the data could not be trained after 45 epochs. More on that can be found in the Report.pdf.

|![WC2 object detection evaluation][WC2-loss-accuracy]|
|:----:|
|**Figure 7 : Loss and accuracy plot of the DetectNet model**|




[//]: (IMAGES)
[sample_data]: ./img/P1-Dataset/dataset_sample.jpg
[sample_evaluate]: ./img/P1-Dataset/P1-Model_GooGLeNet_evaluate.jpg
[WC1-data]: ./img/Workcell1-Classification/dataset/WC1-labels.png
[WC1-loss-accuracy]: ./img/Workcell1-Classification/initial/WC1-1-Loss-Accuracy.png
[WC1-loss-accuray2]: ./img/Workcell1-Classification/Run2/WC1-2-Loss_accuracy.png
[WC2-image-annotation]: ./img/Labelbox/labelbox-robot-person.png
[WC2-loss-accuracy]: ./img/Workcell2-Object-Detection/model/Workcell2-detectNet-Accuracy_loss.png
