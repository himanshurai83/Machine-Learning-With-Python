# Delete a column from a DataFrame.

import pandas as pd

df = pd.read_csv('employee.csv')
print(df)

print("Deleting a column!!")
user = input("From above data enter a column name do you want to delete: ")
df.drop(columns=[user], inplace=True)
print(df)
