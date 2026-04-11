import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, color='green', marker='o', label="Sample data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.title("Sample Data")
plt.legend()
plt.show()
