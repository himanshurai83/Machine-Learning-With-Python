# Count number of employees in each department.
import pandas as pd

df = pd.read_csv('employee.csv')

print(df)

total_count = df.groupby('Department')['Name'].count()
print("Total employee with each department")
print(total_count)
