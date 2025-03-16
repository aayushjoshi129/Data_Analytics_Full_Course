# Video URL: https://youtu.be/bRl2IXIjuqE?si=zc2zn0lonp6ipRFn

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score

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

# Regression Object
regression = LinearRegression()
regression.fit(X_train, y_train)
# Cross Validation
mean_squared_error = cross_val_score(regression, X_train, y_train, scoring='neg_mean_squared_error', cv=10)

print(mean_squared_error)
print(np.mean(mean_squared_error))

# Prediction on Test Data

reg_pred = regression.predict(X_test)

print(reg_pred)

sns.displot(reg_pred - y_test, kind='kde')
plt.savefig("Linear_Regression_Plots/Dist_Plot.jpg")
plt.show()

# The Plot shows that variance is very much less and it lies in between -10 to 10 and there are some outliers also present but most of the data is present within -20 and 10.

score = r2_score(reg_pred, y_test)
print("R2 value is : ", score)