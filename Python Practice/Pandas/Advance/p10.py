# Read multiple CSV files and concatenate them.

import pandas as pd

df1 = pd.read_csv('employee.csv')
df2 = pd.read_csv('employee2.csv')

print("After concat the data!!")
concat_data = pd.concat([df1, df2], axis=0, ignore_index=True)
print(concat_data)
