# This project analyzes student attendance using Pandas and Matplotlib.
# It calculates attendance percentages per student and per class,
# identifies low attendance students, and visualizes attendance trends.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/04. Attendance Tracking System/data.csv')

print("Original Data:")
print(df, "\n")

df["StatusNumeric"] = df["Status"].map({"Present": 1, "Absent": 0})

attendance_per_student = df.groupby("Name")["StatusNumeric"].mean() * 100
attendance_per_class = df.groupby("Class")["StatusNumeric"].mean() * 100

low_attendance_students = attendance_per_student[attendance_per_student < 75]

print("Attendance % per Student:")
print(attendance_per_student, "\n")

print("Attendance % per Class:")
print(attendance_per_class, "\n")

print("Students with Low Attendance (<75%):")
print(low_attendance_students)

# =========================
# 📊 MATPLOTLIB VISUALS
# =========================

# 1️⃣ Bar Chart: Student-wise Attendance
plt.figure()
attendance_per_student.plot(kind="bar")
plt.title("Attendance Percentage per Student")
plt.xlabel("Student")
plt.ylabel("Attendance %")
plt.show()

# 2️⃣ Pie Chart: Class-wise Attendance
plt.figure()
attendance_per_class.plot(kind="pie", autopct="%1.1f%%")
plt.title("Average Attendance by Class")
plt.ylabel("") 
plt.show()