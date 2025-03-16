# Classification - It is the process of dividing datasets into different categories or groups by adding label.

# Decision Tree - Graphical representation of all the possible solutions to a decision.

# Random Forest - Builds multiple decision trees and merges them together. It is more accurate and stable. It corrects habit of Decision Trees of overfitting to their training datasets. ^They get trained with bagging method.

# Naive Bayes - Classification technique based on Bayes' Theorem (Basedon a conditional probability). It assumes the presence of a particular feature in a class is unrelated to the presence of any other features

# K-Nearest Neighbor - Stores all the available cases and classifies new cases based on a similarity measure.

# The K in 'KNN' is the nearest neighbors we wish to take vote from.



# DECISION TREE

# A Decision Tree is a graphical representation of all the possible solutions to a decision based on certain conditions.

# Gini Index: Gini index measures the impurity or randomness of a dataset. In the context of decision trees, it's used as a criterion to evaluate how well a particular feature splits the data into classes (or categories). A lower Gini index indicates a more homogeneous set of samples after the split, which is desirable in decision tree nodes. Gini index can be calculated using the formula:


# Chi-Square (χ²) Test: Chi-square test is used to evaluate the independence between two categorical variables. In decision trees, it's applied in the context of feature selection to assess the significance of the relationship between a feature and the target variable. A higher chi-square value indicates that the feature is more significant in predicting the target variable.


# Information Gain: Information gain measures the reduction in entropy (or uncertainty) achieved by splitting a dataset based on a particular feature. In decision trees, entropy is used as a measure of impurity or disorder in a dataset. Information gain is calculated by comparing the entropy of the dataset before and after the split. A higher information gain suggests that the feature is more informative for predicting the target variable.


# Reduction in Variance: Reduction in variance is a criterion used in decision trees for regression tasks. It measures the decrease in variance achieved by splitting the dataset based on a particular feature. In regression trees, the goal is to minimize the variance of the target variable within each leaf node. The reduction in variance is calculated by comparing the variance of the target variable before and after the split. A higher reduction in variance indicates a better split.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import plot_tree

iris = sns.load_dataset('iris')
# print(iris.head(10))
#
# print(iris.info())
# print(iris.isnull().sum())

# sns.pairplot(data=iris, hue='species')
# plt.savefig('Decision_tree_Plots/Iris_Dataset_Pairplot.jpg')
# plt.show()

# numeric_columns = iris.select_dtypes(include=['float64', 'int64'])
# sns.heatmap(numeric_columns.corr())
# plt.savefig('Decision_tree_Plots/Iris_Dataset_HeatMap_Correlation_Plot.jpg')
# plt.show()

target = iris['species']
df1 = iris.copy()
df1 = df1.drop('species', axis=1)

# print(df1)
# print(target)

le = LabelEncoder()
target = le.fit_transform(target)
# print(target)

y = target

X_train, X_test, y_train, y_test = train_test_split(df1, y, train_size=0.2, random_state=42)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

y_pred = dtree.predict(X_test)
# print(y_pred)

print(classification_report(y_test,y_pred))


fn = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'sepal width (cm)']
cn = ['setosa', 'versicolor', 'virginica']
fig, axes = plt.subplots(nrows=1, ncols=1, figsize= (4,4), dpi=300)
plot_tree(dtree, feature_names=fn, class_names=cn, filled=True)
plt.savefig('Decision_Tree_Plots/Decision_tree_Iris.jpg')
plt.show()

