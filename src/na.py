import pandas as pd
import numpy as np

from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
import os
import sys


def read_data( filename ):

    dataset = pd.read_csv(filename)
    t = dataset[['t']]
    y = dataset[['cases']]
    
    return t,y
    
    
def read_data_ex( filename , h1, h2 ):

    dataset = pd.read_csv(filename)
    t = dataset[['t']]
    y1 = dataset[[h1]]
    y2 = dataset[[h2]]
    
    return t,y1,y2
       
    
def print_data( y, t, color,  title, x_label, y_label ):

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(  t, y, color  )
    plt.show()
    
def print_data_ex(  y1, y2, t, title, x_label, y_label ):

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot( t, y1, 'g'  )
    plt.plot( t, y2, 'b'  )
    plt.show()

   
def pol_regression( y, X, _degree_ ):
   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    poly_reg = PolynomialFeatures(degree=_degree_)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)
    return pol_reg,poly_reg
    

def show_error( y, y_poly_pred ):

    rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
    r2 = r2_score(y,y_poly_pred)
    print( "RMSE: {}".format(rmse))
    print( "R^2:  {}".format(r2))


def print_regression( X, y, pol_reg, poly_reg, the_title, x_l, y_l ):

    plt.scatter(X, y, color='red')
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='blue')
    plt.title(the_title)
    plt.xlabel(x_l)
    plt.ylabel(y_l)
    plt.show()  

def do_pol_reg( t, y, msg, level  ):

    print("[Polinomial regression level: {} ]".format( level ) )
    pol_reg,poly_reg = pol_regression(  y, t, level )   
    y_poly_pred = pol_reg.predict(poly_reg.fit_transform( t ))
    show_error( y, y_poly_pred )
    ayear = pd.DataFrame( [ i for i in range( 1,360 ) ] ) 
    ys = pol_reg.predict( poly_reg.fit_transform( ayear ))
    
    print("Maximum cases ( {} ) estimated: {} at {} days.".format( msg, ys.max(), ys.argmax() + 1) )
    #print_regression( t, y, pol_reg, poly_reg, "Cases Corona", "days", "Cases" )    
    

def find_min_error( t, y ):
    
    best_fit = []
    for level in range(1,20):
        pol_reg,poly_reg = pol_regression(  y, t, level )   
        y_poly_pred = pol_reg.predict(poly_reg.fit_transform( t ))
        best_fit.append( np.sqrt(mean_squared_error(y,y_poly_pred)))
        
    return best_fit.index( min(best_fit) ) + 1

  
def main(argv):

    os.system('cls')

    if len(argv) <= 1:
        print("Wrong execution.")
        return      
       
    filename = argv[1]
    option   = argv[2]
            
    if (  os.path.exists(filename) == False ):
    
        print("csv file does not exist..")
        return
    
    t, y = read_data( filename )
    n = find_min_error ( t, y )  
    do_pol_reg( t, y, option , n )

                         
        
                 
if __name__ == '__main__':
    main(sys.argv)  
    
