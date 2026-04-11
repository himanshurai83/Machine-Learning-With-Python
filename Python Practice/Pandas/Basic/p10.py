# Rename a column emp_id to Employee_ID.
import pandas as pd

df = pd.read_csv('employee.csv')
print(df)
print("After Renaming!!")
df.rename(columns={'ID': 'Emp_ID'}, inplace=True)
print(df)
