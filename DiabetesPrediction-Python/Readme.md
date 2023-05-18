# Diabetes prediction dataset

### A Comprehensive Dataset for Predicting Diabetes with Medical & Demographic Data

**Dataset**: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

*About Dataset*:

The Diabetes prediction dataset is a collection of medical and demographic data from patients, 
along with their diabetes status (positive or negative). The data includes features such as age, gender, 
body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. 
This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. 
This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. 
Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and 
the likelihood of developing diabetes.

*What I did*
- Cleansing data
- Manipulating data
- Visualizing data
- Making a model

### Making model

In this stage I chose logistic regression to make a model. Because my dependent variable is categorical (Consist of 0 and 1).

### About Logistic Regression

Logistic regression estimates the probability of an event occurring, such as diabetes or not diabetes, based on a given dataset of independent variables. Since the outcome is a probability, the dependent variable is bounded between 0 and 1.

### Model Optimization

The dataset consists of 100 000 rows and I split the dataset into three part (train, test and validation set). In general I can say that this dataset is small. For small datasets, ‘liblinear’ is a good choice. When I optimize the model I changed the algorithm from *lbfgs* to *liblinear*.

My purpose in dividing the data into three sets is that when I optimize the model, there is a possibility that the model will memorize the data in the test set and also it is possible that a margin of error in the results I will obtain. After I have optimized and finished the model, I can use the validation set to calculate the accuracy rate with more precision. 
