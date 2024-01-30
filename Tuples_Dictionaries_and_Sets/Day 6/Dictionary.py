# DICTIONARY

# Dictionary allows user to write the data in the form of keys and values.

# It is enclosed in curley brackets.

# keys and values are separated by colon.

# Every key pair is separated by comma.

'''
Employee_Data = {'name':'John', 'age':'24', 'gender':'male'}

print(Employee_Data)
print(Employee_Data['name'])
'''

# ITERATION in Dictionaries

Student = {'name':'John', 'class':'6th', 'roll_no':23}

# printing all key names one by one

'''
for x in Student:
    print(x)

# print(Student.keys())
'''

# printing all values names one by one

'''
for x in Student:
    print(Student[x])
'''

# Using value function

'''
for x in Student.values():
    print(x)
'''

# Using Items function

'''
for x,y in Student.items():
    print(x,y)
'''

# FUNCTIONS IN DICTIONARIES

# get

'''
x = Student.get('name')
print(x)
'''

# items

'''
y = Student.items()
print(y)
print(type(y))
'''

# keys

'''
z = Student.keys()
print(z)
'''

# values

'''
j = Student.values()
print(j)
'''

# copy

'''
k = Student.copy()
print(k)
'''

# setDefault

'''
x = Student.setdefault('roll_no', 24)
print(x)
'''

# update

'''
print(Student)
x = Student.update({'roll_no':25})
print(Student)
'''

# pop

'''
print(Student)
y = Student.pop('roll_no')
print(Student)
'''

# popitem

'''
print(Student)
z = Student.popitem()
print(Student)
'''

# clear

'''
print(Student)
Student.clear()
print(Student)
'''


# NESTED DICTIONARIES

Employees = {
    1:
    {
    'name':'John',
    'age':23,
    'gender': 'male'
    },
    2:
    {
    'name':'Lisa',
    'age':24,
    'gender':'female'
},
    3:
    {
    'name':'Peter',
    'age':22,
    'gender':'male'
}
}

print(Employees)
print(Employees[1])
print(Employees[2])
print(Employees[3])
print(Employees[1]['name'])


