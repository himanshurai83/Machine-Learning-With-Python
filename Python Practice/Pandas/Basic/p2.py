# Read a CSV file and display the first 10 rows.
import pandas as pd

df = pd.read_csv("employee2.csv")
print(df.head(10))
