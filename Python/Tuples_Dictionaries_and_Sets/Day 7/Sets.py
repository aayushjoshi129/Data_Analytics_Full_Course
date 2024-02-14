# SETS are unordered collection of data. Every element in set is unique and mutable.

'''
a = {'Iron Man', 'Hulk', 'Thor', 'Captain America'}
print(a)
print(type(a))

for x in a:
    print(x)
'''

# FUNCTIONS

# add

'''
a.add('SpiderMan')
print(a)
'''

# pop

'''
a.pop()
print(a)
'''

# remove

'''
a.remove('SpiderMan')
print(a)
'''

# discard

'''
a.discard('Hulk')
print(a)
'''

# copy

'''
b = a.copy()
print(b)
'''

'''
a = {'Iron Man', 'Hulk', 'Thor', 'Captain America'}
b = {'Superman', 'Batman', 'Wonder-Woman'}
c = {'Hulk', 'Thor'}
d = {'Superman', 'Thor'}
'''

# isdisjoint

'''
print(a.isdisjoint(b))  # element a does not consist of all the elements that are in b
print(a.isdisjoint(c))
print(a.isdisjoint(d))
'''

# issubset

'''
print(d.issubset(a))
print(c.issubset(a))
'''

# issuperset

'''
print(b.issuperset(a))
print(a.issuperset(c))
'''

# update

'''
a.update(b)
print(a)
'''

# clear

'''
print(a.clear())
print(a)
'''

a = {'Iron Man', 'Hulk', 'Thor', 'Captain America'}
b = {'Superman', 'Batman', 'Wonder-Woman'}
c = {'Hulk', 'Thor', 'Spiderman'}
d = {'Superman', 'Thor'}

# union

'''
print(a.union(c))
'''

# difference

'''
print(a.difference(c))
print(c.difference(a))
'''

# difference update

'''
print(a)
a.difference_update(c)
print(a)
'''

# intersection

'''
print(a.intersection(c))
'''

# intersection update

'''
print(a)
a.intersection_update(c)
print(a)
'''

# symmetric difference

'''
print(a)
x = a.symmetric_difference(c)
print(x)
'''

# symmetric difference update

'''
print(a)
a.symmetric_difference_update(c)
print(a)
'''