import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Python Practice/Matplotlib/Project/sales_dataset.csv")

fig, ax = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Sales Analysis Dashboard", fontsize=16)

revenue_product = df.groupby('Product')['Revenue'].sum()
ax[0, 0].bar(revenue_product.index, revenue_product.values, color='orange')
ax[0, 0].set_title('Product vs Revenue')
ax[0, 0].set_xlabel("Product")
ax[0, 0].set_ylabel("Revenue")


ax[0, 1].bar(df['Product'], df['Units_Sold'])
ax[0, 1].set_title("Best selling product")
ax[0, 1].set_xlabel("Product")
ax[0, 1].set_ylabel("Units Sold")


count_by_region = df['Region'].value_counts()
ax[1, 0].pie(count_by_region, labels=count_by_region.index,
             autopct='%1.1f%%', colors=['gold', 'lightblue', 'lightgreen', 'salmon'])
ax[1, 0].set_title('Sales by Region')

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%d-%b')
ax[1, 1].plot(df['Month'], df['Units_Sold'], marker='o')
ax[1, 1].set_title("Sales Trend Over Time")
ax[1, 1].set_xlabel("Date")
ax[1, 1].set_ylabel("Units Sold")
ax[1, 1].grid(True)
ax[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
