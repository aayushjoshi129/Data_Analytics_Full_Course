# LISTS

# List are collection of ordered and mutable data (can be changed)
# multiple data types can be written in a list

'''
fruits = ["apple", "mango", "banana", 12, 14, 13.14]
print(fruits)
print(type(fruits))
'''

# SLICING LISTS

'''
a = ['Iron Man', 'Captain America', 'Hulk', 'Thor']

print(a[0])
print(a)
print(a[::-1])
print(a[0:3])
'''

# ITERATION METHODS

# 1) ITERATION USING FOR LOOP

'''
a = ['Iron Man', 'Captain America', 'Hulk', 'Thor']
for i in a:
    print(i)
'''

# 2) ITERATION USING FOR LOOP WITH RANGE AND LENGTH FUNCTION

'''
a = ['Iron Man', 'Captain America', 'Hulk', 'Thor']
for i in range(len(a)):
    print(a[i])
'''

# 3) ITERATION USING WHILE LOOP

'''
a = ['Iron Man', 'Captain America', 'Hulk', 'Thor']
i=0
while(i<len(a)):
    print(a[i])
    i+=1
'''

# 4) USING SHORT-HAND FOR LOOP

'''
a = ['Iron Man', 'Captain America', 'Hulk', 'Thor']
[print (i) for i in a]
'''

# FUNCTIONS

'''
a = ['Iron Man', 'Captain America', 'Hulk', 'Thor','Hulk']
print(a)
'''

# 1) TO FIND THE LENGTH OF A LIST

'''
print(len(a))
'''

# 2) TO COUNT AN OCCURENCE OF A PARTICULAR ELEMENT

'''
print(a.count('Hulk'))
'''

# 3) TO ADD TO THE LIST

'''
a.append('Spiderman')
print(a)
'''

# 4) TO ADD TO A SPECIFIC LOCATION IN A LIST

'''
a.insert(1,'Vision')
print(a)
'''

# 5) TO REMOVE TO THE LIST

'''
a.remove('Spiderman')
print(a)
'''

# 6) TO REMOVE FROM A SPECIFIC LOCATION IN A LIST

'''
a.pop(1)
print(a)
'''

# 7) TO CREATE COPY OF A LIST

'''
b=[]
print(b)
b=a.copy()
print(b)
'''

# 8) TO ACCESS AN ELEMENT

'''
print(a.index("Thor"))
'''

# 9) TO EXTEND THE LIST

'''
c=['Vision', 'Spiderman']
a.extend(c)
print(a)
'''

# 10) TO REVERSE THE LIST

'''
a.reverse()
print(a)
'''

# 11) TO SORT THE LIST

'''
a.sort()
print(a)
'''

# 12) TO CLEAR ALL THE DATA FROM THE LIST

'''
a.clear()
print(a)
'''

# LIST COMPREHENSION

'''
l1 = [30, 40, 50, 60]
l2 = []
for i in l1:
    if(i>40):
        l2.append(i)
print(l1,"\n",l2)

l3 = [i for i in l1]
print(l3)

l4 = [i for i in l1 if i>40]
print(l4)
'''