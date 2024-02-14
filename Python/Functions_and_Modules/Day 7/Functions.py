# Functions are a set of code, which once created, they can be used throughout the program.

# Functions help break our program into smaller parts and helps it look more organized and manageable.

'''
def Hello():    # function definition
    print("Hello World")    # function body

Hello()     # function calling
'''

# PARAMETERS AND ARGUMENTS

# Parameters are the variables that are written inside parentheses with the name of the function.

# Arguments are the values passed to the parameters while calling the functions.

'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))


def sum(a, b):
    print(a + b)

sum(a, b)
'''

# ARBITRARY ARGUMENTS

'''
def hello(*name):
    print("Hi", name[1])

hello('John', 'Lisa', 'Caren')
'''

# RETURN STATEMENT AND RECURSION IN PYTHON

# Return statement is used to exit from a function and return the value of the function.

'''
def hello():
    return 'Hello World'
print(hello())
'''


# RECURSION

# RECURSION is most commonly used mathematical and programming concept.
# It means function calling itself, giving us a benefit of looping through data in order to get a result.

'''
def hello():
    print('hello')
    return hello()
print(hello())
'''

'''
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
'''

# LAMBDA FUNCTIONS IN PYTHON

# It is used when an anonymous function is required for a short period of time.
# It can take numerous arguments
# it can only have 1 expression

'''
a = lambda b: b*5
print(a(5))

x = lambda a, b, c: (a+b)*c
print(x(3,2,4))
'''

# LOCAL AND GLOBAL VARIABLES

# Local Variable are restricted to one block of code and cannot be changed throughout the program

# Global Variables are not restricted to one block of code and then can be changed throghout the program

x = 24      # global variables
print(x)
def hello():
    global x
    x = 25  # local variables
    print(x)
hello()
print(x)