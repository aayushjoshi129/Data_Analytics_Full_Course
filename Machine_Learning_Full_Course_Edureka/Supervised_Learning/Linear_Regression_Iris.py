import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

disease = datasets.load_diabetes()
# print(disease)

# from sklearn import datasets, linear_model
# from sklearn.metrics import mean_squared_error

# Load the dataset
disease = datasets.load_diabetes()

# Assigning features and target variables
disease_X = disease.data[:, np.newaxis,2]
disease_Y = disease.target

# Splitting the data
disease_X_train = disease_X[:-30]
disease_X_test = disease_X[-20:]
disease_Y_train = disease_Y[:-30]
disease_Y_test = disease_Y[-20:]

# Creating and fitting the model
reg = linear_model.LinearRegression()
reg.fit(disease_X_train, disease_Y_train)

# Making predictions
y_predict = reg.predict(disease_X_test)

# Calculating mean squared error
mse = mean_squared_error(disease_Y_test, y_predict)
print("Mean Squared Error:", mse)

# Retrieving coefficients and intercept
weights = reg.coef_
intercept = reg.intercept_

print("Weights:", weights)
print("Intercept:", intercept)

plt.scatter(disease_X_test, disease_Y_test)
plt.plot(disease_X_test, y_predict)
plt.savefig("Plots/Linear_Regression.jpg")
plt.show()

