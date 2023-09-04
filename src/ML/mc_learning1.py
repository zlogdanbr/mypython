import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

import os
import sys


def plotHistData( df ):
    df.hist(bins=50, figsize=(20,15))
    plt.show()
    plt.savefig('test.png', bbox_inches='tight')
    
def plotthis( X, y):
    plt.plot(X, y[:, 0], "b--", label="Not Iris-Virginica")
    plt.show()
    plt.savefig('test.png', bbox_inches='tight')


def getDataFrame( filename ):

    df = pd.read_csv(   filename, header=0,  names=['CRC2','Y'] , na_values='.')
    print("Correlation between data.")
    print(df.corr())
    print('\n')
    print("Creating training set...")

    train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
    
    X= train_set[['CRC2']]
    y = (train_set['Y'])   
  
    Xt= test_set[['CRC2']]
    yt = (test_set['Y'])    

    return X,y,Xt,yt

def train(X,y,type):

    ctype = None
    
    if ( type == 0 ):
        ctype = LinearRegression()
    else:
        ctype = LogisticRegression(solver='lbfgs')
        
        
    try:       
        ctype.fit(X, y)
        
        return ctype
  
    except:
        print( "Fatal error.")
        return None
        
        
# program main function just input data
def main(argv):

    os.system('clear')

    if len(argv) <= 1:
        print("Wrong execution.")
        return      
       
    filename = argv[1]
    
    algo = None
    
    if ( os.path.exists(filename)):
        X,y,Xt,yt = getDataFrame(filename)
        algo = train(X,y,0)
        print("Testing data being validated")
        print("{} {}".format( algo.intercept_, algo.coef_))
        print( algo.predict([[10000000]]))

    else:
        print("csv file does not exist..")
        
    
              
if __name__ == '__main__':
    main(sys.argv)



