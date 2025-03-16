# Support Vector Machines (SVM) is a supervised machine learning algorithm used for classification and regression tasks. In short:

# 1. Objective: SVM aims to find the optimal hyperplane that best separates the data points into different classes (for classification) or predicts the target variable (for regression).

# 2. Margin Maximization: SVM seeks to maximize the margin, which is the distance between the hyperplane and the nearest data points (support vectors). By maximizing the margin, SVM aims to achieve better generalization performance and improve robustness to noise.

# 3. Kernel Trick: SVM can handle non-linearly separable data by mapping the input features into a higher-dimensional space using kernel functions. This allows SVM to find non-linear decision boundaries in the original feature space.

# 4. Regularization Parameter: SVM includes a regularization parameter (C) to control the trade-off between maximizing the margin and minimizing classification errors. A smaller value of C leads to a wider margin but may result in more misclassifications, while a larger value of C may lead to a narrower margin but fewer misclassifications.

# 5. Effective in High-Dimensional Spaces: SVM performs well in high-dimensional spaces and is effective for datasets with many features, such as text classification and image recognition tasks.

# 6. Commonly Used Kernels: Commonly used kernels in SVM include linear, polynomial, radial basis function (RBF), and sigmoid kernels, each suitable for different types of data and problem domains.

# In summary, SVM is a powerful and versatile algorithm for both classification and regression tasks, known for its ability to find optimal decision boundaries and handle non-linear data using kernel functions.


# Support Vector Machines (SVM) is a machine learning algorithm used for classification and regression tasks. It aims to find the optimal hyperplane that best separates data points into different classes (classification) or predicts the target variable (regression). SVM maximizes the margin between the hyperplane and the nearest data points (support vectors) and can handle non-linear data using kernel functions. It is effective in high-dimensional spaces and offers flexibility with different kernel options.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn import datasets


iris = datasets.load_iris()
# print(iris['data'])

X = iris['data'][:, (2,3)]    # petal length, petal width
y = iris['target']

# print(y)

# z=np.array([0, 1, 2])

# z1 = (z==0) | (z==1)

# print(z)
# print(z1)

# Let's break down the code:


# ```python
# z=np.array([0, 1, 2])
#
# z1 = (z==0) | (z==1)
#
# print(z)
# print(z1)
# ```
#
# 1. `z=np.array([0, 1, 2])`: This creates a NumPy array `z` containing the elements `[0, 1, 2]`.
#
# 2. `z1 = (z==0) | (z==1)`: This line creates a boolean mask `z1` by performing element-wise comparisons on array `z`.
#    - `(z==0)` checks if each element in `z` is equal to 0, resulting in `[True, False, False]`.
#    - `(z==1)` checks if each element in `z` is equal to 1, resulting in `[False, True, False]`.
#    - The `|` operator performs element-wise logical OR operation between the two conditions, resulting in `[True, True, False]`.
#    - So, `z1` will be `[True, True, False]`.
#
# 3. `print(z)`: This prints the original array `z`, which is `[0, 1, 2]`.
#
# 4. `print(z1)`: This prints the boolean mask `z1`, which is `[True, True, False]`.
#
# So, `z1` contains `True` for elements in `z` that are equal to 0 or 1, and `False` for other elements.

setosta_or_versicolor = (y==0) | (y==1)
# print(setosta_or_versicolor)
X = X[setosta_or_versicolor]
y = y[setosta_or_versicolor]

# plt.scatter(X[:,0][y==0], X[:,1][y==0], label='class 0')
# plt.scatter(X[:,0][y==1], X[:,1][y==1], label='class 1')
# plt.legend()
# plt.savefig('SVM_Plots/SVM_Iris_Plot.jpg')
# plt.show()

# SVM Classifier Model

svm_clf = SVC(kernel="linear", C = 1e6) # max c -> Hard Classifier
svm_clf.fit(X, y)

# print(svm_clf.coef_) # weight arms
# print(svm_clf.intercept_) # bias term


def plot_svc_decision_boundary(svm_clf, xmin, xmax):
    w = svm_clf.coef_[0]
    b = svm_clf.intercept_[0]

    # At the decision boundary, w0*w0 + w1*w1 +b = 0
    # => x1 = -w0/w1 * x0 - b/w1
    x0 = np.linspace(xmin, xmax, 200)
    decision_boundary = -w[0]/w[1] * x0 - b/w[1]

    margin = 1/w[1]
    gutter_up = decision_boundary + margin
    gutter_down = decision_boundary - margin

    svs = svm_clf.support_vectors_

    plt.scatter(svs[:,0], svs[:,1], s=180, facecolors='#FFAAAA', label='Support Vectors') # Highlighting support vectors
    plt.plot(x0, decision_boundary, "k-", linewidth=2, label='Hyperplane')
    plt.plot(x0, gutter_up, "k--", linewidth=2)
    plt.plot(x0, gutter_down, "k--", linewidth=2)


plot_svc_decision_boundary(svm_clf, 0, 5.5)
plt.plot(X[:,0][y==1], X[:,1][y==1], 'bs')
plt.plot(X[:,0][y==0], X[:,1][y==0], 'yo')
plt.xlabel("Petal Length", fontsize='14')
plt.axis([0, 5.5, 0, 2])
plt.legend()
# plt.savefig('SVM_Plots/Decision_Boundary_Iris.jpg')
# plt.show()


# The decision boundary equation in the context of a binary classification problem represents the mathematical expression that separates the data points of different classes in the feature space. For a linear decision boundary in two dimensions, the equation of the decision boundary is typically represented as:

# [ w1 x1 + w2 x2 + b = 0 ]

# Where:
# - ( x1 ) and ( x2 ) are the features (or independent variables) of the data point.
# - ( w1 ) and ( w2 ) are the coefficients (or weights) associated with each feature.
# - ( b ) is the bias term (or intercept) which shifts the decision boundary away from the origin.
# - The decision boundary separates the data points into different classes based on whether the expression is greater than or less than zero.

# In vectorized form, the equation can be expressed as:

# [ {w}^T {x} + b = 0 ]

# Where:
# - ( {w} ) is the weight vector containing the coefficients of each feature.
# - ( {x} ) is the feature vector containing the values of each feature.
# - ( {w}^T ) denotes the transpose of the weight vector.
# - The decision boundary is determined by the linear combination of the features weighted by the corresponding coefficients plus the bias term.

# The decision boundary separates the feature space into regions corresponding to different classes. Data points on one side of the decision boundary are classified as belonging to one class, while data points on the other side are classified as belonging to the other class. The coefficients ( w1 ) and ( w2 ), along with the bias term ( b ), are learned during the training process of the classification model.


print(svm_clf.support_vectors_)

# Why Scaling is Important -- to get the better fit



