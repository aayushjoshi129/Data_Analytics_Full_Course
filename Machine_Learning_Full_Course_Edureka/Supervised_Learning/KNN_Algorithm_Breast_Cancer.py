# KNN - It is a supervised algorithm the classifies a new data point into the target class, depending on the features of it's neighboring data points.

# 1) Non-parametric: KNN is a non-parametric algorithm, meaning it does not make any assumptions about the underlying data distribution.

# 2) Instance-based: KNN is an instance-based algorithm that memorizes the entire training dataset. During prediction, it finds the K nearest neighbors to the query instance and makes predictions based on their majority class (for classification) or average value (for regression).

# 3) Lazy learning: KNN is often referred to as a lazy learning algorithm because it does not learn a discriminative function from the training data. Instead, it defers the learning process until prediction time.

# 4) Simple and easy to understand: KNN is straightforward and easy to understand, making it a popular choice for beginners in machine learning.

# 5) Sensitive to the choice of K: The performance of KNN heavily depends on the choice of the number of neighbors (K). A smaller value of K can lead to a high variance, while a larger value of K can lead to a high bias.

# 6) Not suitable for high-dimensional data: KNN may not perform well on high-dimensional data due to the curse of dimensionality, where the distance between points becomes less meaningful in high-dimensional spaces.

# 7) In summary, KNN is a simple, instance-based algorithm that makes predictions based on the majority vote or average value of the K nearest neighbors. It is easy to understand but sensitive to the choice of K and not suitable for high-dimensional data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

print(cancer.keys())
# print(cancer.data)
# print(cancer.feature_names)
# print(cancer['DESCR'])

df_feat = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
# print(df_feat.head())

df_target = pd.DataFrame(cancer['target'], columns=['Cancer'])
# print(df_target.head())


from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()
scaled_features = scalar.fit_transform(df_feat)
df_feat_scaled = pd.DataFrame(scaled_features,columns=df_feat.columns)

print(df_feat_scaled.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(scaled_features, np.ravel(df_target), test_size=0.3, random_state=105)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

# Predictions

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

cr = classification_report(y_test, y_pred)
print(cr)

cm = confusion_matrix(y_test, y_pred)
print(cm)

ac = accuracy_score(y_test, y_pred)
print(ac*100)



# Choosing a K Value

error_rate = []

for i in range (1,40):
    knn_loop = KNeighborsClassifier(n_neighbors=i)
    knn_loop.fit(X_train, y_train)
    pred_i = knn_loop.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error rate VS K Value')
plt.xlabel('K')
plt.ylabel('Error_Rate')
plt.savefig('KNN_Plots/K_Value_Accuracy_Check.jpg')
plt.show()

