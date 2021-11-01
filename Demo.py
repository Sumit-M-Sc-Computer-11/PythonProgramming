import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show


def TitanicLogistic():
#step 1-Load data
	print("Inside Logistic Function : ")
	Titanic_Data=pd.read_csv("MarvellousTitanicDataset.csv")
	print("First 5 Records Of Dataset")
	print("Titanic_Data.head()")
	print("Total number of records are",alien(Titanic_Data))


       
	
def main():

    print("Logistic case study : ")
    TitanicLogistic()
	
    
if __name__ == "__main__":
    main()
