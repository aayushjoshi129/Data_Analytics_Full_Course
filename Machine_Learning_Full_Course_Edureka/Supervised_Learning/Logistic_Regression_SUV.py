import numpy as np
import pandas as pd
import matplotlib as plt

df = pd.read_csv('../DataSets/suv_data.csv')
# print(df.head(5))
# print(df.isnull().sum())

# Defining Independent Variable X and dependent variable y

X = df.iloc[:, [2,3]].values        # Age and EstimatedSalary Columns (Independent Variable)
# print(X)
y = df.iloc[:,4].values             # Purchased Column (Dependent Variable)
# print(y)

# from sklearn.cross_validation import train_test_split # (Deprecated)
# this has been deprecated using new import

from sklearn.model_selection import train_test_split

X_train, X_test, y_train,y_test = train_test_split(X, y,train_size=0.25, random_state=0)


# Scale your input values for better performances

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)             # for training dataset, we perform fit and transform both where fit calculates mean and standard deviation whereas transform calculates the logic using a formula that is :
#  new value = (old_value - mean)/standard_deviation
#  z = (x - u) / s

X_test = sc.transform(X_test)  # for test dataset, we perform only transform where transform calculates the logic and apply the same logic that has been applied in training dataset


# Import LogisticRegression Model
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state=0)

print(classifier.fit(X_train, y_train))

y_pred = classifier.predict(X_test)

# Import Accuracy Score

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, y_pred)*100)



