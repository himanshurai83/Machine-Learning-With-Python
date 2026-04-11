# Display last 5 rows of a dataset.

import pandas as pd

df = pd.read_csv("employee2.csv")
print(df.tail())
