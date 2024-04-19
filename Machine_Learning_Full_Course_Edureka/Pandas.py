from sklearn import datasets
iris_dataset = datasets.load_iris()

# print(iris_dataset)

x = iris_dataset.data[:,:2] # [a:b,x:y] means we want rows from a to b and we want columns from x to y index

# print(x)

x_count = len(x.flat)
x_min = x[:,0].min() - .5
x_max = x[:,0].max() + .5
x_mean = x[:,0].mean()

print(x_count, x_min, x_max, x_mean)
print()

# checking version of libraries
# python version
import sys
print('Python: ()', format(sys.version))
# scipy
import scipy
print('scipy: ()', format(scipy.__version__))
# numpy
import numpy
print('numpy: ()', format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: ()', format(matplotlib.__version__))
# pandas
import pandas
print('pandas: ()', format(pandas.__version__))
# sklearn
import sklearn
print('sklearn: ()', format(sklearn.__version__))

