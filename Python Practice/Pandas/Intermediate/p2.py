# Drop rows that contain missing values.

import pandas as pd

data = {
    "Name": ['Himanshu', 'Manish', 'Abhinandan', None, 'Anuj', None, 'Suryansh'],
    "Id": [1, 2, 3, None, 5, None, 7],
    "City": ['Noida', 'Ghazipur', 'Delhi', None, 'Ghazipur', None, 'Lahuwar']
}
df = pd.DataFrame(data)
print(df)
df.dropna(axis=0, inplace=True)
print("After dropping missing values!!")
print(df)
