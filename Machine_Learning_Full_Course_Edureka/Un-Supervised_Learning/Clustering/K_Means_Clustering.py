# Clustering in machine learning is a technique used for grouping similar data points together into clusters based on their intrinsic properties or similarity. It's an unsupervised learning method where the algorithm automatically finds patterns in the data without the need for labeled responses. Clustering is useful for tasks such as customer segmentation, anomaly detection, and image segmentation. Popular clustering algorithms include K-means, hierarchical clustering, and DBSCAN.

# Steps Involved in K-Means Clustering
# 1) Choose no. of clusters
# 2) Initialization
# 3) Cluster Assignment
# 4) Move Centres (Centroid Values) (till the time, it get fixed)
# 5) Optimization
# 6) Converge

# Fuzzy C-Means (FCM) clustering is an extension of K-means clustering that allows data points to belong to multiple clusters with varying degrees of membership. In FCM, each data point has a membership value for each cluster, indicating the degree of belongingness to that cluster. FCM assigns cluster centers iteratively based on minimizing the sum of squared distances between data points and cluster centers weighted by their membership values.

# Difference between K-means and Fuzzy C-Means:

# 1) Membership: In K-means, each data point is assigned exclusively to one cluster, while in FCM, each data point has a membership value for each cluster, indicating the degree of belongingness to that cluster.

# 2) Cluster Centers: In K-means, cluster centers are updated by computing the mean of data points assigned to each cluster. In FCM, cluster centers are updated by considering the weighted mean of data points, where weights are the membership values.

# 3) Hard vs. Soft Assignment: K-means performs hard assignment, where each data point is assigned to exactly one cluster. FCM performs soft assignment, allowing data points to belong to multiple clusters with varying degrees of membership.

# In summary, Fuzzy C-Means extends K-means by allowing for soft assignment of data points to clusters, providing more flexibility in capturing complex data structures.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix
# import helper
import warnings
warnings.filterwarnings("ignore")

actors = pd.read_csv('../../DataSets/BollywoodActorRanking.csv')
# print(actors.head())
# print(actors.isnull().sum())
actors.dropna(inplace=True)
# print(actors.isnull().sum())


