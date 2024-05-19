import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset('iris')
# print(df.head(10))
# print(df['species'].unique())

# print(df.isnull().sum())    # No null values is present

# print(df[df['species']!='setosa'])
df = df[df['species']!='setosa']
# print(df.head())

df['species'] = df['species'].map({'versicolor':0, 'virginica':1})
# print(df.head())

# split dataset into independent and dependent dataset

X = df.iloc[:,:-1]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()

from sklearn.model_selection import GridSearchCV

parameter = {'penalty':['l1','l2', 'elasticnet'], 'C':[1,2,3,4,5,6,10,20,30,40, 50], 'max_iter':[100,200,300] }

classifier_regressor = GridSearchCV(classifier, param_grid=parameter, scoring='accuracy', cv=5)

classifier_regressor.fit(X_train, y_train)

print(classifier_regressor.best_params_)

print(classifier_regressor.best_score_)

y_pred = classifier_regressor.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report

score = accuracy_score(y_pred, y_test)
print(score)

print(classification_report(y_pred, y_test))

# EDA
import matplotlib.pyplot as plt

sns.pairplot(df, hue='species')
# plt.savefig('./Logistic_Plots/Pair_Plot_Iris.jpg')
# plt.show()

print(df.corr())