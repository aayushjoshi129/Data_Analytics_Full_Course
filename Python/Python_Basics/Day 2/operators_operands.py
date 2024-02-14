# types of operators
# 1) Arithmetic Operators

print("Addition: ", 10+2)
print("Subtraction (-): ", 10-2)
print("Multiplication (*): ", 10*2)
print("Floor Division (//): ", 10//3)
print("Exponential (**): ", 2**10)
print("Division (/): ", 10/2)
print("Modulus (%): ", 10%2)
print('\n')

# 2) Comparison Operators

print("Less Than (<): ", 10<2)
print("Greater Than (>): ", 10>2)
print("Less Than or Equal To (<=): ", 10<=2)
print("Greater Than or Equal To (>=): ", 10>=2)
print("Not Equal To (!=): ", 10!=2)
print("Equal To (==): ", 10==2)
print('\n')

# 3) Logical Operators

print("And (and): ", 10>2 and 14>7)
print("Or (or): ", 10>22 or 10>2)
print("Not (not): ", not 10>2)
print('\n')

# 4) Assignment Operators
x=6
print("= ", 6)
print("+= ")
print("-= ")
print("*= ")
print('\n')

# 5) Identity Operators
a=1234
b='1234'
c=1234
print('is ', a is b)
print('is ', a is c)
print('is not ', a is not b)
print('is not ', a is not c)
print('\n')

# 6) Membership Operators

name='Ayush'
print('In ', 'a' in name)
print('In ', 'A' in name)
print('Not In ', 'z' not in name)
print('Not In ', 'A' not in name)
print('\n')

# 7) Bitwise Operators

print('BINARY (bin) ', bin(10))
print('AND (&) ', 10&8)
print('OR (|) ', 10|8 )
print('XOR (^) ', 10^8)
print('ZERO FILL LEFT SHIFT (>>) ', 10>>2)
print('ZERO FILL RIGHT SHIFT (<<) ', 10<<2)
print('\n')
