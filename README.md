# Malaria stage classifier

This is the documentation of a Python package to classify RBCs in microscopy images. It includes:

* a package for the stage-specific classification of RBCs (`Malaria_stage_classifier`) with four folders:
    * `Code` which contains four modules and the code file:
      * `NN.py` which initialises the neural network and trains the data
      * `classes.py` which contains classes for evaluating the properties of each RBC
      * `contours.py` which provides functions for the detection of RBCs in an image
      * `extractCuts.py` which provides functions for extracting the most characteristic profiles in the RBC
      * `Malaria_stage_classifier.py`
    * `Logo` which contains the logo for the pop up windows
    * `Neural_networks` which contains the pre-trained neural networks
    * `Sample_images` which contains three sample images

* to use the package, please follow these instructions:
    * download the `Malaria_stage_classifier.zip` folder which contains the code, the logo for the pop up windows, the pre-trained neural networks, and three sample images

# How to use the package

* open the code file `Classification_of_RBCs` in jupyter
* Tab `Settings`:
    * select the file you want to analyse
    * choose the type, in case of header lines in the text file choose the number of header lines
    * select the folder to save your output
* Tab `Show image`:
    * displays the image
* Tab `Threshold image`:
    * use the `Set threshold` button to show the thresholded image
    * optionally, the preset threshold value can be changed manually
* Tab `Detect cells`:
    * the cell detection parameters can be changed manually and set back to default
* Tab `Classify cells`:
    * `Load NN` loads the neural network
    * `Predict stages` predicts the cell stage
    * `Change predictions` provides the possibility to change the prediction by clicking on the cell
    * `Add data to NN` offers the option to add new data to the NN and retrains the NN
      * to use this option, please download the training data from: https://drive.google.com/file/d/1891AI9LPyk25AkYg3Gw4hvg5-V-YGLAS/view?usp=sharing
    * `Save predictions` saves the predictions in a text or csv file and offers the option to analyse new data
