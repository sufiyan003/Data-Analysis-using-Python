# This project analyzes student attendance using Pandas.
# It calculates attendance percentage per student and per class,
# and identifies students with low attendance.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/04. Attendance Tracking System/data.csv')

print("Original Data:")
print(df)
print("\n")

df["StatusNumeric"] = df["Status"].map({"Present": 1, "Absent": 0})

attendance_per_student = df.groupby("Name")["StatusNumeric"].mean() * 100

attendance_per_class = df.groupby("Class")["StatusNumeric"].mean() * 100

low_attendance_students = attendance_per_student[attendance_per_student < 75]

print("Attendance % per Student:")
print(attendance_per_student)
print("\n")

print("Attendance % per Class:")
print(attendance_per_class)
print("\n")

print("Students with Low Attendance (<75%):")
print(low_attendance_students)
