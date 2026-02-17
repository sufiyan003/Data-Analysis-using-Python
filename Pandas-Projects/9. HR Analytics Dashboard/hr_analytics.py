# This project performs HR analytics using Pandas.
# It calculates department-wise average salary, identifies high-potential employees,
# and analyzes experience vs salary trends.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/9. HR Analytics Dashboard/data.csv')

print("Original Data:")
print(df)
print("\n")

df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])

dept_avg_salary = df.groupby("Department")["Salary"].mean()

high_potential = df[(df["ExperienceYears"] >= 5) & (df["Salary"] < 100000)]

df = df.merge(dept_avg_salary.rename("DeptAvgSalary"), on="Department")
above_avg_salary = df[df["Salary"] > df["DeptAvgSalary"]]

print("Department-wise Average Salary:")
print(dept_avg_salary)
print("\n")

print("High-Potential Employees (Exp>=5 & Salary<100k):")
print(high_potential)
print("\n")

print("Employees with Salary Above Department Average:")
print(above_avg_salary)
