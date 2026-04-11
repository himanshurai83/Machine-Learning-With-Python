# Export a DataFrame to Excel file.
import pandas as pd

data = {
    "Department": ['IT', 'IT', 'HR', 'HR'],
    "Employee": ['Aman', 'Anuj', 'Himanshu', 'Manish'],
    "Salary": [50000, 55000, 45000, 48000]
}

df = pd.DataFrame(data)
print(df)
# df.to_excel('sample.xlsx', index=False)

df2 = pd.read_csv('employee.csv')
print(df2)
print("Data save successfully!!")
df2.to_excel('sample.xlsx', index=False)
