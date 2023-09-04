import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os
import sys


def read_data( filename= 'petrol_consumption.csv'):

    dataset = pd.read_csv(filename)
    X = dataset[['Petrol_tax', 'Average_income', 'Paved_Highways','Population_Driver_licence(%)']]
    y = dataset['Petrol_Consumption']
    
    return X,y
    

def train_data( X, y ):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])


def main(argv):

    os.system('cls')

    if len(argv) <= 1:
        print("Wrong execution.")
        return      
       
    filename = argv[1]
       
    if ( os.path.exists(filename)):
        X, y = read_data( filename )
        coef = train_data( X, y )
        print( coef )
    else:
        print("csv file does not exist..")
        
                 
if __name__ == '__main__':
    main(sys.argv)       