# Add a new column Bonus which is 10% of Salary.
import pandas as pd

data = {
    'Name': ['Himanshu', 'Abhinandan', 'Manish', 'Anuj', 'Amit', 'Neha', 'Sumit'],
    'Department': ['IT', 'Finance', 'Management', 'IT', 'Finance', 'Law', 'MBBS'],
    'Salary': [45000, 37000, 65000, 50000, 75000, 45000, 76000]
}
df = pd.DataFrame(data)
print(df)

# first way
print("Adding a bonus column!!")
# df['Bonus'] = df['Salary'] * .1
# print(df)

# Second way
df.insert(3, 'Bonus', df['Salary']*.1)
print(df)
print(df.shape)
