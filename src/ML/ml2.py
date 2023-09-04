# https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

import os
import sys


def read_data( filename,  var_names, output_name):

    dataset = pd.read_csv(filename) 
    X = dataset[ var_names]
    y = dataset[output_name]    
    return X,y
    

def train_data( X, y ):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient']), X_test, y_test, regressor


def predict_from_data(X_test, regressor):

    return regressor.predict(X_test)
    
    
def evaluate_from_data( y_test, y_pred ):

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

def main(argv):

    os.system('cls')

    if len(argv) <= 1:
        print("Wrong execution.")
        return      
       
    filename = argv[1]
    
    var_names = ['Petrol_tax', 'Average_income', 'Paved_Highways','Population_Driver_licence(%)']
    output_name = 'Petrol_Consumption'
       
    if ( os.path.exists(filename)):
        X, y = read_data( filename, var_names, output_name )
        coef, X_test, y_test, regressor = train_data( X, y )
        print( coef )
        y_pred = predict_from_data( X_test, regressor )
        evaluate_from_data( y_test, y_pred )
        
    else:
        print("csv file does not exist..")
        
                 
if __name__ == '__main__':
    main(sys.argv)       