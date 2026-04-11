# Group employees by department and calculate:
# Total salary
# Average salary
# Employee count

import pandas as pd

df = pd.read_csv('employee.csv')
print(df)

print("Total salary!!")
total_salary = df.groupby('Department')['Salary'].sum()
print(total_salary)

print("Average salary!!")
avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)

print("Employee Count!!")
emp_count = df.groupby('Department')['Name'].count()
print(emp_count)
