# CREATION OF DF IN PANDAS

import pandas as pd
import numpy as np

'''
data = {"Name": ["John", "Peter", "Lisa"],
        "Age": [25, 28, 31],
        "Salary": [30000, 45000, 25000]
        }

df = pd.DataFrame(data)
print(df)
'''

'''
data_csv = pd.read_csv('D:/Data_Analytics_Using_Python/pythonProject/DataSets/company.csv')
print(data_csv)
'''

'''
data_excel = pd.read_excel('D:/Data_Analytics_Using_Python/pythonProject/DataSets/expense3.xlsx')
print(data_excel)
'''

# Exploring Data in Pandas

'''
data_excel_ESD = pd.read_excel('D:/Data_Analytics_Using_Python/pythonProject/DataSets/ESD.xlsx')
# print(data_excel_ESD)
# print(data_excel_ESD.head(10))
# print(data_excel_ESD.tail(10))
# print(data_excel_ESD.info())
# print(data_excel_ESD.describe())
print(data_excel_ESD.isnull().sum())
'''

# HANDLING DUPLICATE VALUES IN PANDAS

'''
data_csv = pd.read_csv('D:/Data_Analytics_Using_Python/pythonProject/DataSets/company1.csv')
print(data_csv)
print(data_csv.duplicated())
print(data_csv["EEID"].duplicated().sum())
# print(data_csv["EEID", "gender"].duplicated().sum())
print(data_csv.drop_duplicates())
'''

# WORKING WITH MISSING DATA IN PANDAS

'''
data_csv = pd.read_csv('D:/Data_Analytics_Using_Python/pythonProject/DataSets/company1.csv')
print(data_csv)
print()
print(data_csv.isnull().sum())
print()
print(data_csv.isna().sum())
print()
print(data_csv.dropna())
print()
print(data_csv)
print()
data_csv["salary"] = data_csv["salary"].replace(np.nan, data_csv["salary"].mean())
print(data_csv)
print()
print(data_csv.fillna(method = "bfill"))
print()
# print(data_csv.fillna().bfill())
print()
print(data_csv.fillna(method = "ffill"))
'''

