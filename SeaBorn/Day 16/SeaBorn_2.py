# HEATMAP SEABORN

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
'''
data = sns.load_dataset("tips")
gp = data.groupby('day').agg({"tip":"min"})
print(data,"\n")
print(gp,"\n")
sns.heatmap(gp)
plt.show()
'''

'''
data = pd.read_excel("../../DataSets/ESD.xlsx")
gp = data.groupby("Job Title").agg({"Annual Salary":"mean"})
print(data,"\n")
print(gp,"\n")

sns.heatmap(gp)
plt.show()
'''

# COUNT PLOT SEABORN
'''
data = sns.load_dataset("tips")
print(data)

sns.countplot(data, x='day')
plt.show()
'''

'''
df = pd.read_excel('../../DataSets/ESD.xlsx')
print(df)
sns.countplot(df, x='Department', hue="Gender")
plt.show()
'''

# VIOLIN PLOT SEABORN
'''
data = sns.load_dataset("tips")
print(data)
sns.violinplot(data, x='total_bill')
plt.show()
'''

# PAIR PLOT SEABORN

'''
data = sns.load_dataset("tips")
sns.pairplot(data)
plt.show()
'''

# STRIP PLOT SEABORN
'''
data = sns.load_dataset("tips")
sns.stripplot(data, x='day', y='total_bill', hue='sex')
plt.show()
'''

# BOX PLOT

'''
data = sns.load_dataset("tips")
sns.boxplot(data, x='day', y='tip')
plt.show()
'''

# CAT PLOT SEABORN (CATEGORICAL PLOT)
'''
data = sns.load_dataset("tips")
sns.catplot(data, x='day', y='tip', hue='sex')
plt.show()
'''

# RELATIONAL PLOT
'''
data = sns.load_dataset("tips")
print(data)
sns.relplot(data, x="tip", y="total_bill", hue="sex", col="day")
plt.savefig("Relational_Plot.png")
plt.show()
'''

# SWARM PLOT
'''
data = sns.load_dataset("tips")
print(data)
sns.swarmplot(data, x="day", y="total_bill", hue="sex", dodge=True)
plt.savefig("Swarm_Plot_Dodge.png")
plt.show()
'''

# KDE PLOT  (Kernel Density Estimation)
'''
data = sns.load_dataset("tips")
sns.kdeplot(data, x='total_bill', hue='day', multiple='stack')
plt.show()
'''