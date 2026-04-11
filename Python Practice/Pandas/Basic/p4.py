# Check the shape, columns, and data types of a DataFrame.
import pandas as pd

df = pd.read_csv("employee.csv")
print(f"Shape:{df.shape}, Column:{df.columns}, Data type:{df.dtypes}")
