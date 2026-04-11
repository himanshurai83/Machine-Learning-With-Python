# Replace "Poor" performance with "Needs Improvement".

import pandas as pd

df = pd.read_csv('employee.csv')
print(df)
print("The updated Data!!")
df['Performance'] = df['Performance'].replace("Poor", "Needs Improvement")
print(df)
