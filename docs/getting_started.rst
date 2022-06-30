Malaria stage classifier
========================

This is the documentation of a Python package to classify RBCs in microscopy images. It includes:

* a package for the stage-specific classification of RBCs (`ClassificationRBC`) with four modules:
    * `NN.py` which initialises the neural network and trains the data
    * `classes.py` which contains classes for evaluating the properties of each RBC
    * `contours.py` which provides functions for the detection of RBCs in an image
    * `extractCuts.py` which provides functions for extracting the most characteristic profiles in the RBC
    
Download
========

1. Download `Code` folder which contains the code, the logo for the pop up windows, three pre-trained neural networks, sample images, and a folder for saving the evaluated data from: https://github.com/KatharinaPreissinger/Stage_specific_classification_of_RBCs
2. If you want to retrain the neural network, please download the `Datasets_for_NN` (this requires at least 200 MB of free space)
3. Install jupyter notebook on your computer https://jupyter.org/install
4. Read the documentation for more information about the classes and modules

How to use the package
======================

1. Open the code file `Classification_of_RBCs` in jupyter
2. Tab `Settings`:
    * select the file you want to analyse
    * choose the type, in case of header lines in the text file choose the number of header lines
    * select the folder to save your output
3. Tab `Show image`:
    * displays the image
4. Tab `Threshold image`:
    * use the `Set threshold` button to show the thresholded image
    * optionally, the preset threshold value can be changed manually
5. Tab `Detect cells`:
    * the cell detection parameters can be changed manually and set back to default
6. Tab `Classify cells`:
    * `Load NN` loads the neural network
    * `Predict stages` predicts the cell stage
    * `Change predictions` provides the possibility to change the prediction by clicking on the cell
    * `Add data to NN` offers the option to add new data to the NN and retrains the NN
    * `Save predictions` saves the predictions in a text or csv file and offers the option to analyse new data
