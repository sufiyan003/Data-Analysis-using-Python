# This project performs HR analytics using Pandas and Matplotlib.
# It calculates department-wise average salary, identifies high-potential employees,
# and visualizes department-wise salary distribution.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/09. HR Analytics Dashboard/data.csv')

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
# 📊 MATPLOTLIB VISUAL
# =========================

plt.figure()
dept_avg_salary.plot(kind="bar", color="skyblue")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()