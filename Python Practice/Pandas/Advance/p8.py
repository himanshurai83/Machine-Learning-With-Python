# Create a multi-index DataFrame.
import pandas as pd

data = {
    "Department": ['IT', 'IT', 'HR', 'HR'],
    "Employee": ['Aman', 'Anuj', 'Himanshu', 'Manish'],
    "Salary": [50000, 55000, 45000, 48000]
}

df = pd.DataFrame(data)

# Set MultiIndex
df = df.set_index(['Department', 'Employee'])

print(df)
