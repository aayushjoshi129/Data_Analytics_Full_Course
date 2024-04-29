import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def engine_pred(engine):
    dataset = pd.read_csv("../DataSets/cars.csv")

    X = dataset['Engine']
    X = X.to_frame()
    y = dataset['Power']

    # print(X.head())
    # print(y.head())

    plt.scatter(X, y)
    plt.xlabel("Engine")
    plt.ylabel("Power")
    plt.show()

    model = LinearRegression()

    model.fit(X, y)

    X_test = np.array(engine)
    X_test = X_test.reshape((1,-1))
    return model.predict(X_test)

