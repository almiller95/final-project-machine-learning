# final-project-machine-learning

## Overview
This project analyzes [Breast Cancer Wisconsin (diagnostic) Data Set](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) from Kaggle. First, this project utilized python pandas to clean the data. Then used postgres and AWS to host the cleaned data set. Next, it utilized python pandas, matplotlib, and sklearn to create a machine learning model that will predict if a tumor is benign or malignant based on it's attributes. Finally, this project used Tableau and a Flask app to visualize the findings. 

## ETL

## Machine Learning
For this part of the project, I used a colab notebook to create a machine learning model that will predict if a tumor is benign or malignant based on it's attributes. The code for this can be seen [here](MachineLearning.ipynb). 

First, I did some basic data exploration in order to decide how to best implement the data into a model. I determined that there were three main categories, mean (mean of all cells), se (standard error of all cells), and worst (the worst cell). I decided to break the data into these categories and work with the mean category primarily. I also created a correlation graph in order to see which attributes of the mean subcategory were highly correlated in order to avoid using parameters that depended on one another. From this exploration, I determined that the best attributes to use would be  `perimeter_mean`, `texture_mean`, `compactness_mean`, `symmetry_mean`, and `smoothness_mean` as these did not contain colinearity.

Next, I created a Machine Learning model on the above decsribed subgroup of the mean attributes. I split this data set into testing and training, and used a Random Forrest Classifier to predict the test data. I checked the accuracy of this model, and 91.8%. I then used the SVM model to compare accuracy and got an accuracy of 90.1%. I then decided that I wanted to compare this subgroup of the mean attributes to a model than included all of the mean attributes. When creating the same Machine Learning models, I discovered that using all mean attributes with a Random Forrest Classifier provided 100.0% accuracy, and SVM gave 91.8% accuracy. However, an accuracy of 100.0% is suspicious and is likely a result of using attributes that have multi colinearity. Thus, the model without it is probably a better model than when using all of the attributes.

Finally, I created a third Machine Learning model using the worst category of data. When using this set and all of its attributes, I got 95.9% accuracy using the Random Forrest Classifier and 94.2% accuracy using SVM.

Next steps for these models would be predict the outcome of new tumor and then check the accuracy against whether that tumor was actually Malignant or Benign.

## Data Analysis

## Webpage

## Conclusions
