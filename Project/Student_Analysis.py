import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Python Practice/Matplotlib/Project/student_performance.csv")
# print(df.head())
# print(df.info())

avg_math = df['Math'].mean()
avg_science = df['Science'].mean()
avg_english = df['English'].mean()

# print("Avg_math: ", avg_math)
# print("Avg_english: ", avg_english)
# print("Avg_science: ", avg_science)

df['Total'] = df['English'] + df['Math'] + df['Science']
# print(df.head())
# print("top Student: ", top_student)

subject = ['Math', 'Science', 'English']
avg_marks = [avg_math, avg_science, avg_english]
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

fig.suptitle("Student Analysis")

ax[0, 0].bar(subject, avg_marks, color='blue', edgecolor='black')
ax[0, 0].set_title('Average Marks')
ax[0, 0].set_xlabel("Subject")
ax[0, 0].set_ylabel("Marks")

ax[0, 1].scatter(df['Attendance'], df['Total'], s=60,
                 alpha=0.7, color='red', marker='^')
ax[0, 1].set_xlabel("Attendance")
ax[0, 1].set_ylabel("Total Marks")
ax[0, 1].set_title("Attendance vs Performance")
ax[0, 1].grid(True)


grade_counts = df["Final_Grade"].value_counts()
ax[1, 0].pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%",
             colors=['gold', 'lightblue', 'lightgreen', 'salmon'])
ax[1, 0].set_title("Grade Distribution")


top_student = df.loc[df['Total'].idxmax()]
name = top_student['Name']
math = top_student['Math']
science = top_student['Science']
english = top_student['English']
mark = [math, science, english]
ax[1, 1].bar(subject, mark, color='purple', edgecolor='black')
ax[1, 1].set_title(f"Topper: {name} (Total: {top_student['Total']})")
ax[1, 1].set_xlabel("Subjects")
ax[1, 1].set_ylabel("Marks")
plt.tight_layout()

plt.show()
