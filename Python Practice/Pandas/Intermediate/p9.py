# Change column datatype from float to integer.
import pandas as pd

data = {
    'Name': ['Himanshu', 'Anuj', 'Abhi', 'Himanshu', 'Manish'],
    'Id': [1, 2, 5.5, 4, 5]
}

df = pd.DataFrame(data)

print(df)
print(df.dtypes)
data2 = df.astype({'Id': 'int'})
print(data2)
