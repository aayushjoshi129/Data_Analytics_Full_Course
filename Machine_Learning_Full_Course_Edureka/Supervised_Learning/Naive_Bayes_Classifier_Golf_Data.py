# Naive Bayes is a simple and efficient probabilistic classifier based on Bayes' theorem with a "naive" assumption of feature independence. In short:
#
# 1. Bayes' Theorem: It calculates the probability of a hypothesis (class label) given the evidence (features) using conditional probabilities.
#
# 2. Naive Assumption: Naive Bayes assumes that features are conditionally independent given the class label. This means that the presence of one feature is independent of the presence of other features.
#
# 3. Classification: It predicts the class label for a given instance by selecting the class with the highest posterior probability calculated using Bayes' theorem.
#
# 4. Efficiency: Naive Bayes is computationally efficient and requires a small amount of training data to estimate the model parameters.
#
# 5. Applications: It is commonly used in text classification (spam detection, sentiment analysis), document categorization, and other classification tasks with discrete features.
#
# In summary, Naive Bayes is a simple and effective classification algorithm based on probability theory, making it suitable for many real-world applications.

# The posterior probability is the probability of a hypothesis (or class label) given observed evidence or data. In classification tasks, it represents the likelihood of a particular class given the features of an instance. It's a key concept in Bayesian inference and is used to make predictions in machine learning algorithms like Naive Bayes.


# P(Class∣Features) = [P(Features∣Class)×P(Class)] / [P(Features)]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('../DataSets/golf_df.csv')
# print(df)

# print(df.info)

df = df.apply(lambda x: x.astype('category')) # This code converts all columns in the DataFrame to the categorical data type.

df1 = df.apply(lambda x: x.cat.codes) # This code converts categorical values in each column to numeric codes.

# print(df1)

X = df1[['Outlook', 'Temperature', 'Humidity', 'Windy']]
y = df1['Play']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=0)

model = MultinomialNB()
model_obj = model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(df)
print(X_test)
print(y_pred)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

cr = classification_report(y_test, y_pred)
print(cr)

cm = confusion_matrix(y_test, y_pred)
print(cm)

ac = accuracy_score(y_test, y_pred)
print(ac*100)

