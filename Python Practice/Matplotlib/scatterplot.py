import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
score = [50, 55, 60, 70, 80, 90]

plt.scatter(study_hours, score, color='red', marker='^')
plt.title('Showing score according to study_hours')
plt.xlabel('Study_Hours')
plt.ylabel('Score')
plt.grid(True)
plt.show()
