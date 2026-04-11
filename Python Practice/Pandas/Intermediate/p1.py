# Handle missing values using fillna() with mean.

import pandas as pd

data = {
    "Name": ['Himanshu', 'Manish', 'Abhinandan', None, 'Anuj', None, 'Suryansh'],
    "Id": [1, 2, 3, None, 5, None, 7],
    "City": ['Noida', 'Ghazipur', 'Delhi', None, 'Ghazipur', None, 'Lahuwar']
}
df = pd.DataFrame(data)
print(df)
print('Finding missing values!!')
print(df.isnull())
print("Filling the null value as default values!!")
df['Id'] = df['Id'].fillna(df['Id'].mean(), inplace=True)
df['Name'] = df['Name'].fillna('Unknown', inplace=True)
df['City'] = df['City'].fillna('Not Available', inplace=True)
print(df)
