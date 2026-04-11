# Select a single column and multiple columns from a DataFrame.
import pandas as pd

df = pd.read_csv("employee2.csv")
print(df.head())
print("Printing one column")
print(df['Name'].head())
print("Printing multiple columns!")
print(df[['Name', 'Age', 'Gender']].head())
