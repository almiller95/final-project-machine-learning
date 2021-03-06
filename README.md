# final-project-machine-learning

## Overview
This project analyzes [Breast Cancer Wisconsin (diagnostic) Data Set](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) from Kaggle. First, this project utilized python pandas to clean the data. Then used postgres and AWS to host the cleaned data set. Next, it utilized python pandas, matplotlib, and sklearn to create a machine learning model that will predict if a tumor is benign or malignant based on it's attributes. Finally, this project used Tableau and a Flask app to visualize the findings. 

## ETL
Raw data was orginally provided a csv file format via ftp - (ftp.cs.wisc.edu). Csv file was uploaded to AWS S3, and then extracted into a colab notebook using Spark. Leveraging Spark, the data was modified to drop off a null values and change column header names. Final data was then loaded into an AWS RDS database using a postgres application.

## Machine Learning
This project used a colab notebook to create a machine learning model that will predict if a tumor is benign or malignant based on it's attributes. The code for this can be seen [here](MachineLearning.ipynb). 

The basic data exploration was done in order to decide how to best implement the data into a model. It was determined that there were three main categories, mean (mean of all cells), se (standard error of all cells), and worst (the worst cell). Based on this, the data was broken into these categories and to work with the mean category primarily. A correlation graph was created in order to see which attributes of the mean subcategory were highly correlated in order to avoid using parameters that depended on one another. From this exploration, the best attributes were determined to be  `perimeter_mean`, `texture_mean`, `compactness_mean`, `symmetry_mean`, and `smoothness_mean` as these did not contain colinearity.

Next, the Machine Learning model was created on the above decsribed subgroup of the mean attributes. This data was split into testing and training sets, and a Random Forrest Classifier was used to predict the test data. The accuracy of this model was checked and  found to be 91.8%. The SVM model was then used to compare accuracy and this revealed an accuracy of 90.1%. This subgroup of the mean attributes was then compared to a model than included all of the mean attributes. Creating the same Machine Learning models, it was discovered that using all mean attributes with a Random Forrest Classifier provided 100.0% accuracy, and SVM gave 91.8% accuracy. However, an accuracy of 100.0% is suspicious and is likely a result of using attributes that have multi colinearity. Thus, the model without it is probably a better model than when using all of the attributes.

Finally, a third Machine Learning model was created using the worst category of data. When using this set and all of its attributes, an accuracy of 95.9% was found when using the Random Forrest Classifier and and accuracy of 94.2% using SVM.

Next steps for these models would be predict the outcome of new tumor and then check the accuracy against whether that tumor was actually Malignant or Benign.

## Data Analysis
To include an interactive element for data exploration, a tableau story is embedded into the web app. This includes a few Tableau dashboards that give the viewer the opportunity to explore the data set themselves. The first dashboard is a summary of the dataset (number of records, tumor types, and attributes). It also includes a dynamic scatterplot that can filter based off of mean input and diagnosis. This can be utilitized to see correlation between specific inputs. The second dashboard is a correlation heatmap of all potential inputs for the model. The user can filter on tumor diagnosis and input category (mean, standard errror, and worst). The third dashboard is focused solely on the mean category and highlights the inputs selected for the machine learning model with mean variables. 

## Webpage
The website uses elements learned from class and implements HTML, CSS, and Flask to help build the body of the website. From there, we use EC2 to host our flask app so the site is available to the public and does not need to be hosted on a local device.
## Conclusions
