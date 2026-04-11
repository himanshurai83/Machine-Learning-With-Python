# Create a pivot table showing department vs average salary.
import pandas as pd

df = pd.read_csv('employee.csv')
print(df)

print("Total salary!!")
total_salary = df.groupby('Department')['Salary'].mean()
print(total_salary)
