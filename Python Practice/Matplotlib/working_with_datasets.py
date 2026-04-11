import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_dataset.csv')
# print(df)
product = df['Product']
units_sold = df['Units_Sold']

# plt.bar(product, units_sold, color='pink')
# plt.pie(units_sold, labels=product, autopct='%1.1f%%')
plt.title('Product sale unit')
plt.xlabel('Product')
plt.ylabel('Units_sold')
plt.legend()
plt.show()
