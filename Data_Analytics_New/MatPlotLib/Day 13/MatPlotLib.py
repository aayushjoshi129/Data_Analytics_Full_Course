# DATA VISUALIZATION - It is the graphical representation of information and data.

# MATPLOTLIB - It is an open-source, low-level graph plotting library in python that serves as a visualization utility.

# MATPLOTLIB was created by John D. Hunter.

'''
import matplotlib.pyplot as plt

y = [98, 67, 88, 95, 88]
x = ["Part1", "Part2", "Part3", "Part4", "Part5"]

# plt.bar(x, y, color='green')
colors=['red', 'blue', 'green', 'yellow', 'magenta']
plt.bar(x, y, color=colors, edgecolor='black')
plt.xlabel("Parts of Harry Porter", fontsize=10)
plt.ylabel("Popularity", fontsize=10)
plt.title("Popularity of Different Parts of Harry Porter", fontsize=17)
plt.show()
'''

# BAR PLOT

'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("../../DataSets/expense3.xlsx")
df = pd.DataFrame(data)
print(df.head(10))

groupby = df.groupby("Payment Mode")["Amount"].sum()

print(groupby)

plt.bar(groupby.index, groupby.values)
# plt.xlabel("Payment Mode")
# plt.ylabel("Amount")
# plt.title("Mode_Amount")
plt.show()
'''

# LINE PLOT

'''
import matplotlib.pyplot as plt

x= ["day1", "day2", "day3", "day4", "day5"]
y= [300, 420, 250, 230, 400]
y1= [320, 120, 150, 330, 200]
plt.plot(x,y, marker='o', color='blue', label='week1')
plt.plot(x,y1, marker='o', color='green', label='week2')
plt.legend()
# plt.show()
'''

'''
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("../../DataSets/expense3.xlsx")
print(df.head(10))
groupby = df.groupby("Category")["Amount"].sum()
print(groupby)
plt.plot(groupby.index, groupby.values)
plt.show()
'''

# SCATTER PLOT

'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.random.randint(1,10, 50)
y = np.random.randint(10,100, 50)
color = np.random.randint(10, 100, 50)

# plt.scatter(x, y, cmap='viridis', c=color)
# plt.colorbar()
# plt.show()

df = pd.read_excel("../../DataSets/ESD.xlsx")
print(df)
plt.scatter(df["Age"], df["EEID"])
plt.colorbar()
plt.show()

'''


# PIE CHART
'''
import matplotlib.pyplot as plt
import pandas as pd
brands=["OnePlus", "Apple", "Nokia", "Samsung", "Redmi"]
x=[22, 35, 30, 3, 10]
c=["red", "blue", "green", "violet", "brown"]
plt.pie(x, labels=brands, colors=c, shadow=True, autopct="%.2f")
plt.show()
'''
