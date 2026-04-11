# Use value_counts() on performance column.

import pandas as pd

df = pd.read_csv('employee.csv')
print(df)

print("Printing the count!!")
print(df['Performance'].value_counts())
