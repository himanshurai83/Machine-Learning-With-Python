# Extract employees whose names start with letter "A".
import pandas as pd

df = pd.read_csv('employee.csv')
data = df[df['Name'].str.startswith('A')]
print(data)
