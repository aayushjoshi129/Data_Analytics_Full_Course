# DATA VISUALIZATION - It is the graphical representation of information and data.

# SEABORN - It is a python data visualization library based on MatPlotLib. It provides a high-level interface for drawing attractive and informative statistical graphics.

# LINE PLOT IN SEABORN
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

'''
data = {"Days": [1,2,3,4,5],
        "NOP": [50,40,60,30,44]
        }
df = pd.DataFrame(data)
# print(df)

sns.lineplot(data, x="Days", y="NOP")
plt.show()
'''

# BAR PLOT
'''
data = sns.load_dataset("tips")
print(data)
sns.barplot(data, x="day", y="tip", hue='sex')
plt.plot()
plt.show()
'''

# HIST PLOT
'''
data = sns.load_dataset('tips')
sns.histplot(data, x='day', hue='sex', kde=True)
plt.show()
'''

'''
data = sns.load_dataset('titanic')
sns.histplot(data, x='age', hue='who', kde=True)
plt.show()
'''

# SCATTER PLOT
'''
data = sns.load_dataset("tips")
print(data)
sns.scatterplot(data, x='total_bill', y='tip', hue='smoker')
plt.savefig("SNS_SCATTER_PLOT.png")
plt.show()
'''