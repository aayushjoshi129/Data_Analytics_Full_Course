
import matplotlib.pyplot as plt

# LEGEND
'''
x = [1,2,3,4,5]
y = [45, 67, 33, 67, 12]
y1 = [41, 60, 13, 66, 13]

plt.plot(x,y, label='male')
plt.plot(x,y1, label='female')
plt.legend()
plt.show()
'''

# SUB PLOT
'''
x=[1,2,3,4,5]
y=[45, 34, 56, 23, 45]

plt.subplot(1,2,1)  # rows, cols, chart_no.
plt.title("Ages")
plt.plot(x,y)

plt.subplot(1,2,1)
x=[6, 7, 8, 9, 10]
y=[65, 74, 26, 43, 85]
plt.subplot(1,2,2)
plt.title("Weights")
plt.suptitle("Humans")
plt.plot(x,y)
plt.savefig("SubPlot.png")  # To save a chart
plt.show()
'''

