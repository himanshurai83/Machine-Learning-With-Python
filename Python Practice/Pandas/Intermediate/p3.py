# Sort employees by salary in descending order.

import pandas as pd

df = pd.read_csv('employee.csv')
print(df)
print("Sorting salary in descending order!!")
sorted_data = df.sort_values(by='Salary', ascending=False)
print(sorted_data.head())

# print("Sorting Id in descending order!!")
# sorted_id = df.sort_values(by='ID', ascending=True)
# print(sorted_id)
