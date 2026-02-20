# This project analyzes student academic performance using Pandas and Matplotlib.
# It cleans missing values, calculates averages, determines pass/fail status,
# and visualizes student performance using bar charts and histograms.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/01. Student Performance Analysis/data.csv')

print("Original Data:")
print(df, "\n")

df.fillna(df.mean(numeric_only=True), inplace=True)

print("After Handling Missing Values:")
print(df, "\n")

df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)

df["Result"] = (df["Average"] >= 50) & (df["Attendance"] >= 75)
df["Result"] = df["Result"].map({True: "Pass", False: "Fail"})

top_students = df[df["Average"] >= 80]

print("Final Student Data:")
print(df, "\n")

print("Top Performing Students:")
print(top_students)

# =========================
# 📊 MATPLOTLIB VISUALS
# =========================

# 1️⃣ Bar Chart: Average marks per subject
subject_averages = df[["Math", "English", "Science"]].mean()

plt.figure()
subject_averages.plot(kind="bar")
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# 2️⃣ Histogram: Distribution of student averages
plt.figure()
plt.hist(df["Average"], bins=5)
plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.show()