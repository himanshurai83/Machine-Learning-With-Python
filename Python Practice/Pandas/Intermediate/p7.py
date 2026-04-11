# Apply a function to increase salary by 5%.
import pandas as pd

df = pd.read_csv('employee.csv')

print(df)


def increment_salary(percent):
    df['Salary'] += df['Salary']*(percent/100)


user = int(input("Enter salary percent: "))
increment_salary(user)
print("After incrementing the salary!!")
print(df)
