# This project cleans and analyzes employee data using Pandas and Matplotlib.
# It handles missing values, converts data types,
# and visualizes department-wise average salary.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/03. Employee Dataset Cleaner & Analyzer/data.csv')

print("Original Data:")
print(df, "\n")

df["Salary"].fillna(df["Salary"].mean(), inplace=True)

df["JoiningDate"].fillna("2021-01-01", inplace=True)
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])

print("After Cleaning:")
print(df, "\n")

dept_avg_salary = df.groupby("Department")["Salary"].mean()

high_salary_employees = df[df["Salary"] > 70000]

print("Department-wise Average Salary:")
print(dept_avg_salary, "\n")

print("High Salary Employees:")
print(high_salary_employees)

# =========================
# 📊 MATPLOTLIB VISUAL
# =========================

plt.figure()
dept_avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()