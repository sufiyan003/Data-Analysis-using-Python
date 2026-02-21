# This project analyzes student academic performance using Pandas and Seaborn.
# It cleans missing values, calculates averages, determines pass/fail status,
# and visualizes student performance using bar plots and histograms.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/01. Student Performance Analysis/data.csv')

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
# 📊 SEABORN VISUALS
# =========================

sns.set_style("whitegrid")

# 1️⃣ Bar Plot: Average marks per subject
subject_avg = df[["Math", "English", "Science"]].mean().reset_index()
subject_avg.columns = ["Subject", "Average Marks"]

plt.figure(figsize=(7, 5))
sns.barplot(data=subject_avg, x="Subject", y="Average Marks")
plt.title("Average Marks per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# 2️⃣ Histogram: Distribution of student averages
plt.figure(figsize=(7, 5))
sns.histplot(df["Average"], bins=5, kde=True)
plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()