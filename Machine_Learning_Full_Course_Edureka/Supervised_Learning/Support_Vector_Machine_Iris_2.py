import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())

sns.pairplot(data=iris, hue='species', palette='Set2')
# plt.savefig('SVM_2_Plots/SVM_Pairplot_Iris.jpg')
# plt.show()

from sklearn.model_selection import train_test_split

x=iris.iloc[:,:-1]
y=iris.iloc[:,4]
x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.30)

from sklearn.svm import SVC
model=SVC()

model.fit(x_train, y_train)

y_pred=model.predict(x_test)

# Importing the classification report and confusion matrix
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test, y_pred))

