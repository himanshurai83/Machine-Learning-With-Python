# Remove duplicate rows.
import pandas as pd

data1 = {
    'Name': ['Himanshu', 'Anuj', 'Abhi', 'Himanshu', 'Manish'],
    'Id': [1, 2, 3, 4, 5]
}
df1 = pd.DataFrame(data1)
print(df1)
print('Checking duplicate data!!')
print(df1.duplicated())

print("Deleting duplicate data")
print(df1.drop_duplicates())


data2 = {
    'Name': ['Himanshu', 'Anuj', 'Abhi', 'Himanshu', 'Manish'],
    'Id': [1, 2, 3, 1, 5]
}
df2 = pd.DataFrame(data2)
print(df2)
print('Checking duplicate data!!')
print(df2.duplicated())

print("Deleting duplicate data")
print(df2.drop_duplicates())
