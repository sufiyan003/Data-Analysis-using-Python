# This project performs HR analytics using Pandas and Seaborn.
# It calculates department-wise average salary, identifies high-potential employees,
# and visualizes department-wise salary distribution using a boxplot.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/09. HR Analytics Dashboard/data.csv')

print("Original Data:")
print(df, "\n")

df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])

dept_avg_salary = df.groupby("Department")["Salary"].mean()

high_potential = df[(df["ExperienceYears"] >= 5) & (df["Salary"] < 100000)]

df = df.merge(dept_avg_salary.rename("DeptAvgSalary"), on="Department")
above_avg_salary = df[df["Salary"] > df["DeptAvgSalary"]]

print("Department-wise Average Salary:")
print(dept_avg_salary, "\n")

print("High-Potential Employees (Exp>=5 & Salary<100k):")
print(high_potential, "\n")

print("Employees with Salary Above Department Average:")
print(above_avg_salary, "\n")

# =========================
# 📊 SEABORN VISUAL
# =========================

sns.set_style("whitegrid")

# Boxplot: Salary distribution per Department
plt.figure(figsize=(10, 6))
sns.boxplot(x="Department", y="Salary", data=df, palette="pastel")
plt.title("Salary Distribution per Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()