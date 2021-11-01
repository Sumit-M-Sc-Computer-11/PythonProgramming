# ===================
# Imports
# ===================
import numpy as np
import pandas as pd
import seaborn as sb
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.model_selection import(train_test_split)
from sklearn.model_selection import LogisticRegression 
from sklearn.matrix import accuracy_score

# ===================
# ML Operation
# ===================
def TitanicLogistic():

    line="*"*50
    print("Logistic Regression with Titanic Dataset",line)
   
    # STEP 1 - Load Data
    titanic_Data = pd.read_csv("MarvellousTitanicDataset.csv")

    # Data Analysis
    print("First 5 record of Dataset \n")
    print(titanic_Data.head())
   
    print("Total number of records are : ",len(titanic_Data))
    print("Dataset information \n",line)
    print(titanic_Data.info())

    # STEP 2 - Analyse the data in detail
    print("\nVisualization of survived and non-survived passengers \n", line)
    figure()
    countplot(data=titanic_Data,x="Survived")
    show()

    print("\nVisualization of According to sex \n", line)
    figure()
    countplot(data=titanic_Data,x="Sex")
    show()
    
    print("\nVisualization of According to Passanger class \n", line)
    figure()
    countplot(data=titanic_Data,x="Pclass")
    show()

    print("\nSurvived vs Non_Survived based on age")
    figure()
    titanic_Data["Age"].plot.hist()
    show()
   
    pclass=pd.get_dummies(titanic_Data[Pclass])
    print("pclass.head()")


# =========================
# Step 3-Data Cleaning
# =========================

    titanic_Data.drop("zero",axis=1,inplace=True)
    print("Data After column removal")
    titanic_Data.head()

    sex=pd.get_dummies(titanic_Data["Sex"])	 
    print("Sex.head()")
    sex=pd.get_dummies(titanic_Data["Sex",drop_first==True])
    print("Sex Column After Updation")
    print("Sex.head()")
 
    titanic_Data=pd.concat([(titanic_Data,Sex,Pclass),Axis=1)])


    print("Data after concatination")
    print("titanic_Data.head()")

# Removing unnecessary fields
    titanic_Data.drop(["Sex","sibsp","Parch","Embarked","Pclass"],axis=1, inplace=True)

    print("\nData After column drop",line)
    print(titanic_Data.head())

    # Divide the dataset into X and y
    X = titanic_Data.drop("Survived", axis = 1)
    y = titanic_Data["Survived"]

    # split the data for training and testing purpose
    xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.05)

    print("\nDataset split Size",line, len(xtrain), len(xtest), len(ytrain), len(ytest))

    # Get the model object
    obj = LogisticRegression(max_iter=1000)

    # STEP 4 - Train the dataset
    obj.fit(xtrain, ytrain)

    # STEP 5 - Testing
    output = obj.predict(xtest)

    # Get the Accuracy of model
    print("\nAccuracy of given dataset is : ",line)
    print(accuracy_score(ytest, output))
     

# =============
# Entry Point
# =============
def main():

    TitanicLogistic()
   
# ==========
# Starter
# ==========
if(__name__=="__main__"):
    main()