# Filter rows where salary is greater than 50, 000.
import pandas as pd

df = pd.read_csv("employee.csv")
print(df)

print("Print employee which have salary greater than 50000!!")

# single condition
print(df[df['Salary'] > 50000])


print("Print employee which have salary greater than 60000 and IT department!!")

# Multiple condition
print(df[(df['Salary'] > 60000) & (df['Department'] == "IT")])
