import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Python Practice/Matplotlib/Project/student_performance.csv")
# print(df.head())

df['Total Marks'] = df['Math'] + df['Science'] + df['English']
# print(df.head())

normalized_marks = (df['Total Marks'] - np.min(df['Total Marks'])) / (np.max(
    df['Total Marks'] - np.min(df['Total Marks'])))
# print(normalized_marks)


# fig, ax = plt.subplots(2, figsize=(10, 8))

print(df.head())
grade = df['Final_Grade'].value_counts()
print(grade)
plt.pie(grade, labels=grade.index, autopct="%1.1f%%")
plt.title("Mark Distribution")
plt.show()

# ax[0].plot(normalized_marks, marker='o')
# ax[0].set_title("Normal Form")
# ax[0].set_xlabel("Students")
# ax[0].set_ylabel("Marks")


# ax[1].bar(df.index, df['Total Marks'], edgecolor='black')
# ax[1].set_title("Original")
# ax[1].set_xlabel("Student")
# ax[1].set_ylabel("Marks")
# plt.show()
