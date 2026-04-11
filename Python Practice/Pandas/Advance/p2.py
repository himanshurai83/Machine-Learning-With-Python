# Perform inner join and left join on two DataFrames.
import pandas as pd

data1 = {
    'Id': [1, 2, 3, 4, 5],
    'Name': ['Himanshu', 'Manish', 'Abhi', 'Surya', 'Anuj'],
    'Marks': [45, 66, 78, 90, 76]
}

df1 = pd.DataFrame(data1)
print("Displaying First dataframe!!")
print(df1)

data2 = {
    'Id': [1, 2, 3, 4, 5, 6, 7, 8],
    'Course': ['MCA', 'BCA', 'MBA', 'BBA', 'O-LEVEL', 'B-TECH', 'BSC', 'BA']
}

df2 = pd.DataFrame(data2)
print("Displaying Second dataframe!!")
print(df2)

print("Performing inner join!!")
inner_data = pd.merge(df1, df2, on='Id', how='inner')
print(inner_data)

print("Performing left join!!")
left_data = pd.merge(df1, df2, on='Id', how='left')
print(left_data)
