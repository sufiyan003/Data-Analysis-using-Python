# This project analyzes sales data using Pandas and Matplotlib.
# It calculates revenue, handles missing values,
# and visualizes product-wise and time-based sales performance.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/02. Simple Sales Report/data.csv')

print("Original Data:")
print(df, "\n")

df["Quantity"].fillna(0, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df["Revenue"] = df["Quantity"] * df["Price"]

print("After Cleaning & Revenue Calculation:")
print(df, "\n")

product_sales = df.groupby("Product")["Revenue"].sum()
region_sales = df.groupby("Region")["Revenue"].sum()
daily_sales = df.groupby("Date")["Revenue"].sum()

best_product = product_sales.idxmax()

print("Product-wise Sales:")
print(product_sales, "\n")

print("Region-wise Sales:")
print(region_sales, "\n")

print("Best Selling Product:", best_product)

# =========================
# 📊 MATPLOTLIB VISUALS
# =========================

# 1️⃣ Bar Chart: Product-wise Revenue
plt.figure()
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# 2️⃣ Line Chart: Revenue over Time
plt.figure()
daily_sales.plot()
plt.title("Sales Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()