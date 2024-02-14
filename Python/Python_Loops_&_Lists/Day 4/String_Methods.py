a="Sonu or Titu ki Sweety"
print(a)
print(type(a))

# STRING METHODS

# 1) LENGTH

print(len(a))

# 2) COUNT

print(a.count('o'))

# 3) UPPER

print(a.upper())

# 4) LOWER

print(a.lower())

# 5) INDEX

print(a.index("wee"))

# 6) CAPITALIZE

print(a.capitalize())

# 7) CASEFOLD (CONVERT INTO LOWER)

print(a.casefold())

# 8) FIND

print(a.find('ty'))

# 9) FORMAT (WRITE VARIABLE INSIDE A STRING)

name='John'
age=24
# string = 'my name is ', name
string = 'my name is {}. and my age is {}'
print(string.format(name, age))

# 10) CENTER (FILLS THE GIVEN CHARACTERS AND AND CENTRALIZE A STRING)

print(name.center(20, '*'))
print(name.center(20, '*'))
