

# 1) WAP to find max and min in a set

'''
a = {12, 56, 34, 8, 90, 1, 57}
print(max(a))
print(min(a))
'''

# 2) WAp to find common elements in 3 lists using sets

'''
a = [1, 5, 6, 8, 2]
b = [4, 5, 6, 7]
c = [1, 9, 6, 2, 5]

print(set(a) & set(b) & set(c))
'''

# 3) WAP to find the difference between two sets

'''
a = {1, 5, 6, 8, 2}
c = {1, 9, 6, 2, 5}
print(a.difference(c))
print(c.difference(a))
'''

# 4) WAP to remove an item from a set if it is present in the set

'''
a = {1, 5, 6, 8, 2}
a.discard(5)
print(a)
'''

# 5) WAP to check if a set is a subset of another set

'''
a = {1, 2, 3, 4, 5, 6}
b = {2, 3, 4}
print(a.issubset(b))
print(b.issubset(a))
'''
