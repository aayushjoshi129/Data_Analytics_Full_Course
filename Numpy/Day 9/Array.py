# An Array is defined as a collection of items that are stored at the contiguous emmory locations

# It is a container which can hold a fix number of items, and these items should be of same type.

# A combination of arrays saves a lot of time. They can reduce the overall size of the code.

# It uses much less memory. It is used for creation of n-dim arrays.

# finding elements in numpy array is easy.


# CREATION, INDEXING AND SLICING OF NUMPY ARRAYS

import numpy as np

'''
arr = np.array([10,20,30,40])

print(arr)
print(type(arr))
print(arr[0:3])
print(arr[::-1])

print(arr.shape)
'''

'''
arr2 = np.array([[10,20,30,40], [50,60,70,80]])

print(arr2)
print(type(arr2))
print(arr2[0:2, 0:2])
print(arr2[0:3, 0:3])
print(arr2[0, 0:2])
print(arr2[1, 0:2])

print(arr2.shape)
print(arr2.size)
print(arr2.ndim)
print(arr2.dtype)

'''

# INSPECTING AN ARRAY

'''
arr = np.array([10,20,30,40])
arr2 = np.array([[10,20,30,40], [50,60,70,80]])

# length
print(len(arr))
print(len(arr2))

# shape
print(arr.shape)
print(arr2.shape)

# dimension
print(arr.ndim)
print(arr2.ndim)

# dtype
print(arr.dtype)
print(arr2.dtype)

# size
print(arr.size)
print(arr2.size)

# casting
print(arr.astype(float))
print(arr2.astype(float))
'''

# MATHEMATICAL OPERATIONS AND FUNCTIONS ON ARRAYS

'''
arr1 = np.array([10,20,30,40])
arr2 = np.array([[10,20,30,40], [50,60,70,80]])
arr3 = np.array([3])

print(arr1 + arr2)
print(np.add(arr1, arr2))
print(np.subtract(arr2, arr1))
print(np.multiply(arr1, arr2))
print(np.divide(arr1, arr2))
print(np.power(arr1, arr3))
print(np.sqrt(arr1))
print(np.sqrt(arr2))
'''

# COMBINING AND SPLITTING ARRAYS

'''
arr1 = np.array([30, 40, 50])
arr2 = np.array([5, 5, 3])

print(np.concatenate([arr1, arr2])) # Concatenate
print(np.concatenate([arr1, arr2], axis=0)) # Concatenate

arr3 = np.array([[30, 40], [50, 10]])
arr4 = np.array([[5, 5], [3, 3]])
print(np.concatenate([arr3,arr4]))  # Concatenate
print(np.concatenate([arr3,arr4],axis=1)) # Horizontal Concatenate
print(np.hstack([arr3,arr4]))   # Horizontal Concatenate
print(np.vstack([arr3,arr4]))   # Vertical Concatenate

a = np.array([30,40,30,40,10,20])
print(np.array_split(a,4))
print(np.array_split(a,3))
'''

# ADDING AND REMOVING ELEMENTS IN THE ARRAY

# Functions
# np.append(h,g)  -   append items to an Array
# np.insert(a,1,5)    -   Inserts item in an Array
# np.delete(a,[1]) - Delete items from an Array

a = np.array([20,40,60,80])
b = np.array([[20,40],[60,80]])
print(np.append(a,[100,120]))   # Append
print(np.insert(a,1,[100,120])) # Insert
print(np.insert(b,1,[100,120], axis=1)) # Insert
print(np.insert(b,1,[100], axis=1)) # Insert
print(np.delete(a,1))   # Delete
print(np.delete(b,1, axis=1))    # Delete

