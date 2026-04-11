import matplotlib.pyplot as plt

product = [1, 2, 3, 4, 5, 6]
sales = [10, 20, 30, 4, 5, 100]

plt.bar(product, sales, color='purple', label='Bar chart')
plt.title("Sales Data")
plt.xlabel("product")
plt.ylabel("Sales")
plt.legend()
plt.show()
