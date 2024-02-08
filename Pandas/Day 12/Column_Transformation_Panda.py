import pandas as pd

'''
df = pd.read_excel("../../Datasets/ESD.xlsx")
# print(df,"\n")

df.loc[(df["Bonus %"]==0),"getBonus"]="No Bonus"
df.loc[(df["Bonus %"]>0),"getBonus"]="Bonus"
print(df.head(10))
'''

'''
df = pd.read_excel("../../Datasets/Practice1.xlsx")
print(df,"\n")
df["Full_Name"] = df["First_Name"].str.capitalize() + " " + df["Last_Name"].str.capitalize()
print(df,'\n')

df["Bonus"] = (df["Salary"]/100)*20
print(df,'\n')

data = {"Months":["January", "February", "March", "April"]}
a = pd.DataFrame(data)
print(a,'\n')

def extract(value):
    return value[0:3]

a["Short_Month"]=a["Months"].map(extract)
print(a,'\n')
'''

# GROUP BY FUNCTIONS IN PANDAS

'''
data = pd.read_excel("../../Datasets/ESD.xlsx")
print(data.head(10),'\n')

gp = data.groupby(["Department","Gender"]).agg({"EEID":"count"})
print(gp,'\n')

gp1 = (data.groupby("Country").agg({"Annual Salary":"mean"}).sort_values("Annual Salary", ascending=False))
print(gp1,'\n')

gp2 = (data.groupby(["Country","Gender"]).agg({"Annual Salary":"mean"}).sort_values("Annual Salary"))
print(gp2,'\n')
'''

# MERGE, JOIN AND CONCATENATE IN PANDAS

# MERGE
'''
data1 = {"Emp_Id": ["E01","E02","E03","E04","E05","E06"],
         "Names": ["Ram", "Shyam", "Rahul", "Vishal", "Ravi", "Garvit"],
         "Age": [34,56,23,44,32, 43]
         }

data2 = {
"Emp_Id": ["E01","E07","E03","E04","E08","E06"],
    "Salary":[45000, 56000, 34000, 30000, 50000, 60000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1,'\n')
print(df2,'\n')

print("Inner Join\n",pd.merge(df1, df2, on="Emp_Id", how="inner"))
print("Left Join\n",pd.merge(df1, df2, on="Emp_Id", how="left"))
print("Right Join\n",pd.merge(df1, df2, on="Emp_Id", how="right"))
print("Outer Join\n",pd.merge(df1, df2, on="Emp_Id", how="outer"))
'''

# CONCATENATE
'''
data1 = {"Emp_Id": ["E01","E02","E03","E04","E05","E06"],
         "Names": ["Ram", "Shyam", "Rahul", "Vishal", "Ravi", "Garvit"],
         "Age": [34,56,23,44,32, 43]
         }

data2 = {"Emp_Id": ["E07","E08","E09","E10","E11","E12"],
         "Names": ["Bittu", "Chintu", "Pappu", "Chhotu", "Bunty", "Golu"],
         "Age": [34,56,23,44,32, 43]
         }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1,'\n')
print(df2,'\n')

print(pd.concat([df1, df2]))
'''

# Compare DataFrames in Pandas
'''
dict = {"Fruit": ["Mango", "Apple", "Banana", "Papaya"],
        "Price": [100, 150, 50, 35],
        "Quantity": [15, 10, 10, 3]
        }

df1 = pd.DataFrame(dict)
df2 = df1.copy()
print(df1,'\n')
print(df2,'\n')

df2.loc[0, "Price"]=120
df2.loc[1, "Price"]=175
df2.loc[3, "Price"]=30
df2.loc[0, "Quantity"]=12
df2.loc[1, "Quantity"]=15
df2.loc[3, "Quantity"]=5

print(df2,'\n')

print(df1.compare(df2))
print(df1.compare(df2,align_axis=0))
'''

# PIVOTING AND MELTING DATAFRAMES

# PIVOTING
'''
dict = {
    "keys": ["k1", "k2", "k1", "k2"],
    "Names":["John", "Ben", 'David', "Peter"],
    "Houses":["red", "blue", "green", "red"]
}

df1 = pd.DataFrame(dict)
print(df1,'\n')

print(df1.pivot(index="keys", columns="Names", values="Houses"))
# print("Pivot\n", df1.pivot("keys", "Names", "Houses"))
'''

# MELTING
'''
dict = {
    "Names":["John", "Ben", 'David', "Peter"],
    "Houses":["red", "blue", "green", "red"],
    "Grades": ["3rd", "8th", "9th", "8th"]
}

df1 = pd.DataFrame(dict)
print(df1,'\n')

print(pd.melt(df1, id_vars=["Names"], value_vars=["Houses","Grades"], var_name="Houses&Grades", value_name="value"))
'''

