# Video URL: https://www.youtube.com/watch?v=J_ESMRGpl74&list=PLTDARY42LDV7WGmlzZtY-w9pemyPrKNUZ&index=6

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)

dataset = pd.read_csv("../DataSets/boston_house_prices.csv")
# print(dataset.head(10))

# Independent Features and Dependent features

X = dataset.drop('MEDV', axis=1)
y = dataset['MEDV']
# print("X:",X)
# print("y:",y)

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)

# scalar.inverse_transform(X_train) # To Inverse the transformed value

X_test = scalar.transform(X_test)

ridge_regressor = Ridge()

parameters = {'alpha':[1,2,5,10,20,30,40,50,60,80,90]}

ridge_cv = GridSearchCV(estimator=ridge_regressor, param_grid=parameters, scoring='neg_mean_squared_error', cv=5)

rv = ridge_cv.fit(X_train, y_train)

print("Best Alpha Value is: ",ridge_cv.best_params_)
print("Best Score is: ",ridge_cv.best_score_)

ridge_pred = ridge_cv.predict(X_test)

print(ridge_pred)

sns.displot(ridge_pred - y_test, kind='kde')
plt.savefig("Linear_Regression_Plots/Ridge_Regression_Dist_Plot.jpg")
plt.show()

score = r2_score(ridge_pred, y_test)
print("R2 value is : ", score)