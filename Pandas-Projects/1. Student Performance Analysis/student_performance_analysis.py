# This project analyzes student academic performance using Pandas.
# It loads student data from a CSV file, cleans missing values,
# calculates averages, and identifies pass/fail students.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/1. Student Performance Analysis/data.csv')

print("Original Data:")
print(df)
print("\n")

df.fillna(df.mean(numeric_only=True), inplace=True)

print("After Handling Missing Values:")
print(df)
print("\n")

df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)

df["Result"] = (df["Average"] >= 50) & (df["Attendance"] >= 75)

df["Result"] = df["Result"].map({True: "Pass", False: "Fail"})

top_students = df[df["Average"] >= 80]

print("Final Student Data:")
print(df)
print("\n")

print("Top Performing Students:")
print(top_students)
