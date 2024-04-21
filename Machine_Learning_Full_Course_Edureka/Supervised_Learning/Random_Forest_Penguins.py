# Random Forest - It is constructed using multiple decision tree's and the final decision is obtained by majority votes of the decision trees.

# Feature Selection
# 1) In Classification - By default, the feature selection is taken as the square root of total number of all the features.

# 2) In Regression - By Default, features are selected by the total number of all the features divided by 3.

# Ensemble techniques, particularly Random Forest, are a type of machine learning approach that involves combining multiple individual models to improve overall performance. Specifically, Random Forest is an ensemble learning method that constructs a multitude of decision trees during training and outputs the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.

# In essence, Random Forest works by training a large number of decision trees, each on a random subset of the training data and a random subset of the features. During prediction, each tree "votes" on the outcome, and the final prediction is determined by aggregating the votes. This approach leads to better generalization and robustness compared to individual decision trees.

# Overall, Random Forest is a powerful ensemble learning technique that is widely used for classification and regression tasks due to its ability to handle complex datasets, mitigate overfitting, and provide reliable predictions.

# Overfitting in machine learning is when a model learns the training data too well, capturing noise and irrelevant patterns, which leads to poor performance on new data. It happens when the model becomes overly complex and memorizes the training examples instead of learning the underlying patterns. To address overfitting, techniques like simplifying the model and regularization are used to find the right balance between complexity and generalization ability.



# HANDS ON

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('penguins')
# print(df.head(5))
# print(df.shape)
# print(df.isnull().sum())
df.dropna(inplace=True)
# print(df.isnull().sum())

# Feature Engineering

# One Hot Encoding to Transform Categorical Data into Numerical Data (Sex, Island)

# print(pd.get_dummies(df['sex']).head())

sex = pd.get_dummies(df['sex'], drop_first=True)
# print(sex)

# print(pd.get_dummies(df['island']).head())

island = pd.get_dummies(df['island'], drop_first=True)
# print(island)

new_data = pd.concat([df, sex, island], axis=1)
# print(new_data)

# dropping the repeated columns i.e., island, sex

new_data.drop(['island', 'sex'], axis=1, inplace=True)

# print(new_data.shape)


# Creating separate target variable

Y = new_data.species
# print(Y.unique())

Y = Y.map({'Adelie':0, 'Chinstrap':1, 'Gentoo':2})
# print(Y.unique())

new_data.drop(['species'], axis=1,  inplace=True)
print(new_data.shape)

X = new_data

# Splitting Dataset into Training and Testing Data

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.3, random_state=0)

# Training Random Forest Classifier on Training Dataset

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=5, criterion='entropy', random_state=0)

classifier.fit(X_train, y_train)

# Predictions

y_pred = classifier.predict(X_test)
print(y_pred)

# Confusion Matrix

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)

ac = accuracy_score(y_test, y_pred)
print(ac*100)

cr = classification_report(y_test, y_pred)
print(cr)


# Try with different number of trees and gini criteria

classifier_gini = RandomForestClassifier(n_estimators=7, criterion='gini', random_state=0)
classifier_gini.fit(X_train, y_train)

y_gini_pred = classifier_gini.predict(X_test)
print(accuracy_score(y_test, y_gini_pred)*100)

# with more trees,k the model is giving more accurate results

