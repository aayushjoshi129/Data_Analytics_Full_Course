# Numpy is the short form of Numerical Python

# In 2005, Travis Oliphant created Numpy package

# Numpy is a package that defines a multi dimension array object and associates fast math and functions that operate on it.

# It also has functions for working in a domain of linear algebra, fourier transformations and matrices.

# In Simple Words, It is the fundamental package for scientific computing in python

'''
import numpy as np
a = np.array([20, 30, 40])
b = np.array([50, 60, 70])
print(a+b)

l1 = [20, 30, 40]
l2 = [50, 60, 70]
print(l1+l2)

'''

# NUMPY - SORT, FILTER AND SEARCH

import numpy as np

'''
ar1 = np.array([7,8,4,12,9])
ar2 = np.array([[7,8,4,12,9], [76,23,56,11,66]])
print(ar1)
print(np.sort(ar1)) # Sort
print(ar2)
print(np.sort(ar2)) # Sort
print('\n'
      )
s = np.where(ar1==4)    # Search
print(s)

ar3 = np.array([2,3,4,5,6,7,8])
ss = np.searchsorted(ar3,5) # SearchSorted
print(ss)

ar4 = np.array([20,30,40,50])
fa1 = [True, False, True, False] # Filtered Array
new1 = ar4[fa1]
print(new1)

fa2 = ar4>35    #  Filtered Array
new2 = ar4[fa2]     
print(new2)

'''

# AGGREGATION FUNCTIONS IN NUMPY

'''
a = np.array([30,40,60,70])
print(np.sum(a))    # SUM
print(np.min(a))    # MIN
print(np.max(a))    # MAX
print(np.size(a))   # SIZE
print(np.mean(a))   # MEAN
print(np.cumsum(a)) # CUMSUM (CUMULATIVE SUM)
print(np.cumprod(a))    # CUMOROD (CUMULATIVE PRODUCT)

b = [100, 150, 199, 200, 250, 130]
c = [10, 50, 30, 40, 30, 10]

price = np.array(b)
quantity = np.array(c)
print(price, '\n', quantity)
print(np.cumsum([price,quantity]))
print(np.cumprod([price,quantity], axis=0))
d = np.cumprod([price,quantity], axis=0)
print((d[1].sum()))

'''


# STATISTICAL FUNCTIONS IN NUMPY

import statistics as stats

baked_food = [200, 300, 130, 200, 300, 280]
a = np.array(baked_food)
print(a)
print(np.mean(a))   # sum of all values/total no. of values
print(np.mean(baked_food)) # sum of all values/total no. of values
print(np.median(a)) # Median
print(np.median(baked_food)) # Median
print(stats.mode(a))    # Mode
print(stats.mode(baked_food))    # Mode
print(np.std(a))    # Standard Deviation (It is the data spread quantity)
print(np.std(baked_food))    # Standard Deviation (It is the data spread quantity)
print(np.var(a))    # Variance  (Square of Standard Deviation)
print(np.var(baked_food))    # Variance (Square of Standard Deviation)
print(63.1796**2)

# Coefficient of Correlation

# Negative (-) value represents inversely proportional relationships
# Positive (+) value represents proportional relationships
# Zero (0) 0 means no relationships

tobacco_consumption = [30, 50, 10, 30, 50, 40]
deaths = [100, 120, 70, 100, 120, 112]

print(np.corrcoef([tobacco_consumption, deaths]))

price = [300, 100, 350, 150, 200]
sales = [10, 20, 7, 17, 3]
print(np.corrcoef([price,sales]))