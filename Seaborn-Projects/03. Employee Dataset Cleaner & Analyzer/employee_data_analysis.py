# This project cleans and analyzes employee data using Pandas and Seaborn.
# It handles missing values, converts data types,
# and visualizes department-wise salary distribution using box plots.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/03. Employee Dataset Cleaner & Analyzer/data.csv')

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
# 📊 SEABORN VISUAL
# =========================

sns.set_style("whitegrid")

plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="Department", y="Salary")
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()