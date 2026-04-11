# Find average salary of employees.
import pandas as pd

df = pd.read_csv('employee.csv')
print(df)
print("Average Salary!")
avg_salary = df['Salary'].mean()
print(avg_salary)
