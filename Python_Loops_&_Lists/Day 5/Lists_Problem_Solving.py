a = ['Ross', 'Rachel', 'Monica', 'Joe']

# 1) WAP to swap first and fourth element

'''
print(a)
a[0],a[3]=a[3],a[0]
print(a)
'''

# 2) WAP to add a new value at second position

'''
print(a)
a.insert(1,'Phoebe')
print(a)
'''

# 3) WAP to delete a value from third position

'''
print(a)
a.pop(2)
print(a)
'''

b = [13, 7, 12, 10]

# 1) WAP to multiply all the numbers in a list

'''
mult=1
for i in b:
    mult*=i
print(mult)
'''

# 2) WAP to get the largest no from the list

'''
print(max(b))
b.sort()
# or
print(b[-1])
'''

# 3) WAP to get the smallest no from the list

'''
b.sort()
print(b[1])
# or
print(min(b))
'''
