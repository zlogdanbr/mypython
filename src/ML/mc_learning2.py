import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def plot( csvfile ):

    df = pd.read_csv(csvfile, sep=',')
    df.describe()

    plt.scatter(df['var1'], df['var2'])
    plt.xlabel('var1')
    plt.ylabel('var2')
    plt.title('From the goods')
    plt.show()

def regression(path):

    df = pd.read_csv(path, sep=',')

    X = df[list(df.columns)[:-1]]
    y = df['var3']

    X_train, X_test, y_train, y_test = train_test_split(X,y)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_predictions = regressor.predict(X_test)

    print('var3:', regressor.score(X_test, y_test))

def main():
    path = "D:\dev\data\irisorig.data"
    regression(path)

main()