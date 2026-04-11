# Find maximum and minimum salary department-wise.

import pandas as pd

df = pd.read_csv("employee.csv")

print(df)

print("Printing maximum salary of each department!!")
max_salary = df.groupby('Department')['Salary'].max()
print(max_salary)

print("Printing minimum salary of each department!!")
max_salary = df.groupby('Department')['Salary'].min()
print(max_salary)
