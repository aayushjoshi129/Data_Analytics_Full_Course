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