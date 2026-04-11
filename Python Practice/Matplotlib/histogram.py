import matplotlib.pyplot as plt

x = [40, 45, 43, 56, 54, 34, 56, 78, 54, 64.45, 54, 67, 89]

plt.hist(x, label='Student', color='blue')
plt.title("Checking Frequency")
plt.xlabel('Score')
plt.ylabel('No. of student')
plt.legend()
plt.show()
