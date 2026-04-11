# Use loc and iloc to select specific rows and columns.
import pandas as pd

df = pd.read_csv('employee.csv')
print(df)

print(df.loc[2, 'Name'])
print(df.iloc[0, 1])
