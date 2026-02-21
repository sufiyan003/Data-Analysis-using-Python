# This project analyzes student attendance using Pandas and Seaborn.
# It calculates attendance percentages per student and per class,
# identifies low attendance students, and visualizes attendance trends.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/04. Attendance Tracking System/data.csv')

print("Original Data:")
print(df, "\n")

df["StatusNumeric"] = df["Status"].map({"Present": 1, "Absent": 0})

attendance_per_student = (
    df.groupby("Name")["StatusNumeric"].mean() * 100
).reset_index()

attendance_per_class = (
    df.groupby("Class")["StatusNumeric"].mean() * 100
)

low_attendance_students = attendance_per_student[
    attendance_per_student["StatusNumeric"] < 75
]

print("Attendance % per Student:")
print(attendance_per_student, "\n")

print("Attendance % per Class:")
print(attendance_per_class, "\n")

print("Students with Low Attendance (<75%):")
print(low_attendance_students)

# =========================
# 📊 SEABORN + MATPLOTLIB VISUALS
# =========================

sns.set_style("whitegrid")

# 1️⃣ Bar Plot: Student-wise Attendance (Seaborn)
plt.figure(figsize=(9, 5))
sns.barplot(
    data=attendance_per_student,
    x="Name",
    y="StatusNumeric"
)
plt.title("Attendance Percentage per Student")
plt.xlabel("Student")
plt.ylabel("Attendance %")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2️⃣ Pie Chart: Class-wise Attendance (Matplotlib)
plt.figure(figsize=(6, 6))
plt.pie(
    attendance_per_class.values,
    labels=attendance_per_class.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Average Attendance by Class")
plt.tight_layout()
plt.show()