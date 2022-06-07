# Stage-specific classification of RBCs

This is a documentation of a Python package to classify RBCs in microscopy images. It includes:

* a package for the stage-specific classification of RBCs (`ClassificationRBC`) with four modules:
    * `NN.py` which initialises the neural network and trains the data
    * `classes.py` which contains classes for evaluating the properties of each RBC
    * `contours.py` which provides functions for the detection of RBCs in an image
    * `extractCuts.py` which provides functions for extracting the most characteristic profiles in the RBC
