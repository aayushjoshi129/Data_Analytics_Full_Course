# Implementing Logistic Regression
# 1) Collecting data
# 2) Analyzing Data
# 3) Data Wrangling
# 4) Train and Test
# 5) Accuracy Check

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn import datasets

titanic = sns.load_dataset('titanic')

titanic_data = pd.DataFrame(titanic)
# print(titanic_data)
# print(titanic_data.head(10))
print(titanic_data.columns)

print("# of Passengers in original data: "+str(len(titanic_data.index)))


# ANALYZING DATA

# custom_colors = ["blue", "orange"]
# sns.countplot(x='survived', data=titanic_data, hue='survived', palette=custom_colors)
# plt.savefig("Plots/Count_Plot_Survived_Or_Not.jpg")
# plt.show()

# custom_colors = ["blue", "orange"]
# sns.countplot(x='survived', data=titanic_data, hue='sex')
# plt.savefig("Plots/Count_Plot_Survived_Or_Not_Sex.jpg")
# plt.show()

# custom_colors = ["blue", "orange"]
# sns.countplot(x='survived', data=titanic_data, hue='pclass')
# plt.savefig("Plots/Count_Plot_Survived_Or_Not_Pclass.jpg")
# plt.show()

# titanic_data["age"].plot.hist()
# plt.savefig("Plots/Age_Histogram.jpg")
# plt.show()

# titanic_data["fare"].plot.hist()
# plt.savefig("Plots/Fare_Histogram.jpg")
# plt.show()

# sns.countplot(x="sibsp", data=titanic_data)
# plt.savefig("Plots/Count_Plot_sibsp")
# plt.show()


# Data Wrangling

print(titanic_data.isnull().sum())

# sns.heatmap(titanic_data.isnull(), yticklabels=False, cmap="viridis")
# plt.savefig("Plots/Heat_Map_Null.jpg")
# plt.show()


# sns.boxplot(x='pclass', y='age', data=titanic_data)
# plt.savefig("Plots/Box_Plot.jpg")
# plt.show()

titanic_data.dropna(inplace=True)
# print(titanic_data.isnull().sum())

# sns.heatmap(titanic_data.isnull(), yticklabels=False, cmap="viridis")
# plt.savefig("Plots/Heat_Map_Removing_Null.jpg")
# plt.show()


# Converting required columns into Categorical Values

sex = pd.get_dummies(titanic_data['sex'], drop_first=True)
print(sex)

embark = pd.get_dummies(titanic_data['embarked'], drop_first=True)
print(embark)

pcl = pd.get_dummies(titanic_data['pclass'], drop_first=True)
print(pcl)


titanic_data = pd.concat([titanic_data, sex, embark, pcl],axis=1)
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)
# print(titanic_data.head(2))
# print(titanic_data.columns.tolist())


titanic_data.drop(['embarked', 'sex', 'who', 'adult_male', 'embark_town', 'class', 'deck', 'alive', 'alone', 'pclass'], axis=1, inplace=True)
# print(titanic_data)


# TRAINING AND TESTING DATA

# TRAINING
X = titanic_data.drop('survived', axis=1)
# print(X)
# X.columns = X.columns.astype(str)
y = titanic_data['survived']

# Assuming X is your input data (e.g., DataFrame or array)

# Convert feature names to strings
X.columns = X.columns.astype(str)

y.index = y.index.astype(str)
# from sklearn.cross_validation import train_test_split
# this has been deprecated using new import

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression(max_iter=10000)

# print(y)
print(logmodel.fit(X_train, y_train))

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(accuracy_score(y_test, predictions)*100)

