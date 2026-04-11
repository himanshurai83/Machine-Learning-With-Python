import matplotlib.pyplot as plt

regions = ['North', 'South', 'West', 'East']
revenue = [3000, 2000, 1500, 1000]

plt.pie(revenue, labels=regions, autopct='%1.1f%%')
plt.title('Revenue Analysis')
plt.legend()
plt.show()
