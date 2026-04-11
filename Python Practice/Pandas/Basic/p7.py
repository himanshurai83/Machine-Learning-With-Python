# Find all employees whose performance rating is "Excellent".

import pandas as pd

df = pd.read_csv("employee.csv")
print(df)

print("Printing employee with excellent!!")

print(df[df['Performance'] == "Excellent"])
