# Create a DataFrame from a dictionary containing student names and marks.

import pandas as pd

data = {
    "Name": ['Himanshu', 'Manish', 'Abhinandan'],
    "Marks": [75, 80, 90]
}

df = pd.DataFrame(data)
print(df)
