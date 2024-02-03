# 1) WAP to check if a given no is odd or even

"""
number = int(input("Enter Number: "))
if (number%2==0):
    print(number, " number is even")
else:
    print(number, " number is odd")
print("\n")
"""

# 2) WAP to check whether a number is positive

"""
if (number>=0):
    print(number, " number is positive")
else:
    print(number, " number is negative")
print("\n")
"""

# 3) WAP to create area calculator

"""
figure = input("Enter Figure name (Rectangle or Square): ")
if figure=='Rectangle':
    length=int(input("Enter Length of Rectangle: "))
    breadth=int(input("Enter breadth of Rectangle: "))
    print("Area of Rectangle is ", length*breadth)
elif figure=='Square':
    side=int(input("Enter Side of Square: "))
    print("Area of Square is ", side*side)
else:
    print("Enter correct figure name")
print("\n")
"""

# 4) WAP to check passed letter is vowel or not

"""
letter = input("Enter Letter: ")
if letter.upper() in ('A', 'E', 'I', 'O', 'U'):
# if letter.upper() in ("AEIOU"):
    print(letter, " Given Letter is a Vowel")
else:
    print(letter, " Given letter is a consonant")
print("\n")
"""

# 5) Check given number is a single digit number, or a 2 digit number, upto 5 digit.

num=int(input("Enter Number upto 5 digits: "))

if 0 <= num <= 9:
    print(num, " is a single digit number")
elif 10 <= num <= 99:
    print(num, " is a double digit number")
elif 100 <= num <= 999:
    print(num, " is a triple digit number")
elif 1000 <= num <= 9999:
    print(num, " is a four digit number")
elif 10000 <= num <= 99999:
    print(num, " is a five digit number")
else:
    print("Enter a valid number within given range")
print("\n")