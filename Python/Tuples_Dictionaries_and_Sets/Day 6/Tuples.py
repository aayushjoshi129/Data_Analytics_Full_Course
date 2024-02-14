# TUPLES

# Tuples are the collection of ordered and un-mutable or immutable data

# for tuples, no brackets are mandatory. By choice one can use paranthesis.

# Once created, tuples cannot be changed

# Multiple datatypes can be written in a tuple

'''
a = 'apple', 'mango', 'banana', 1, 6, 7, 3.5
b = ('apple', 'mango', 'banana', 1, 6, 7, 3.5)

print(type(a))
print(type(b))


# How to make a tuple with 1 element

c = 'tuple',    # add comma to make tuple
print(type(c))
'''

# SLICING AND ITERATION IN TUPLES


# d = ('OnePlus', 'Vivo', 'Redmi', 'SamSung', 'Nokia')

'''
print(d[1:3])
print(d[::-1])
print(d[::2])
'''

# LOOPS

# WITH FOR LOOP

'''
for i in d:
    print(i)
'''

'''
for i in range(len(d)):
    print(d[i])
'''

# WITH WHILE LOOP

'''
i=0
while(i<len(d)):
    print(d[i])
    i+=1
'''

# CONVERSION OF TUPLES AND TUPLE FUNCTIONS

# d = ('OnePlus', 'Nokia', 'Redmi')

'''
print(type(d))
print(d)
e = list(d)
print(type(e))
e.append('Vivo')
print(e)
f = tuple(e)
print(type(f))
print(f)
'''

# TUPLE FUNCTIONS

'''
d = ('OnePlus', 'Nokia', 'Redmi', 'Redmi')
print(d.count('Nokia'))
print(d.count('Redmi'))
print(d.index('Redmi'))
'''
