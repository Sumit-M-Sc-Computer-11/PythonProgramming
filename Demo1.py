# ===================
# Imports
# ===================
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from seaborn import countplot


# ===================
# ML Operation
# ===================
def TitanicLogistic():

    print("Logistic Regression with Titanic Dataset")
   
    # STEP 1 - Load Data
    Titanic_Data = pd.read_csv("MarvellousTitanicDataset.csv")

    # Data Analysis
    print("First 5 record of Dataset \n")
    print(Titanic_Data.head())
   
    print("Total number of records are : ",len(Titanic_Data))
    print("Dataset information: \n ",Titanic_Data.info())
    print("Visualization of Servived and non servived passangers")
    figure()
    countplot(Data=Titanic_Data,x="survived")
    show()				

# =============
# Entry Point
# =============
def main():

    TitanicLogistic()
   
   
# ==========
# Starter
# ==========
	if(__name__ == "__main__"):
    	    main()