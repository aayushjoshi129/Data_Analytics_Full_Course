# Modules are the py files, that contains set of functions that you want to include in your program

# IN - BUILT MODULES IN PYTHON

# Datetime

'''
import datetime

x = datetime.datetime.now()
print(x)
print(x.day)
print(x.month)
print(x.year)
print(x.time())
print(x.time().hour)
print(x.time().minute)
print(x.time().second)
print(x.time().microsecond)

y = datetime.datetime(1997,2,6)
print(y)
print(y.strftime("%A"))
print(y.strftime("%a"))
print(y.strftime("%B"))
print(y.strftime("%b"))
print(y.strftime("%C"))
print(y.strftime("%c"))
'''


# Random

'''
import random
l = ['Heads', 'Tails']
x = random.randint(1,10)
y = random.choice(l)
print(x)
print(y)
'''

# Math

'''
import math
x = max(1,77,88)
print(x)
y = min(1,77,88)
print(y)
z = pow(2,10)
print(z)
ab = math.sqrt(16)
print(ab)
ac = math.sqrt(99)
print(ac)
ad = abs(-14)
print(ad)

f = math.floor(23.778)
print(f)

c = math.ceil(23.778)
print(c)

'''


# CREATION OF MODULES

# To create a module, you need to create a py file in similar path to your python file. Inside that you can add required functions you need your program to perform.

# To call module inside your program, use import keyword followed by the py filename.

