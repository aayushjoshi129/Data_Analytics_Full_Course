# BOX PLOT

import matplotlib.pyplot as plt
import numpy as np

'''
l = [25, 46, 12, 44, 23, 13, 12, 14, 15, 16, 17, 88, 56, 77, 34, 35, 22, 17]
plt.boxplot(l)
plt.show()
'''

# HISTOGRAM PLOT
'''
x = [1,2,3,4,5,6,7,8,90,22,33,44,55,66,77,12,34,65]
plt.hist(x,bins=10)
# plt.hist2d(x,bins=20)
plt.show()
'''

# VIOLIN PLOT
'''
a = [20,30,40,50, 60, 10, 20, 30, 50, 60, 0, 0]
plt.violinplot(a)
plt.show()
'''

# STEM PLOT
'''
a = [20,30,40,50, 60, 10, 20, 30, 50, 60, 0, 0]
plt.stem(a)
plt.show()
'''

# STACK PLOT
'''
days = [1,2,3,4,5,6,7]
NOP1 = [5,10,20,30,35,60,80]
NOP2 = [10,20,30,25,40,50,90]
NOP3 = [8,30,50,60,70,90,100]
NOP4 = [20,30,40,10,30,60,100]
plt.stackplot(days, NOP1, NOP2, NOP3, NOP4)
plt.show()
'''

# STEP PLOT
'''
x=["day1", "day2", "day3", "day4", "day5"]
y=[30,40,25,30,40]
plt.step(x,y)
plt.show()
'''

# Day 15
# LEGEND