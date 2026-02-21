# This project analyzes sales data using Pandas and Seaborn.
# It calculates revenue, handles missing values,
# and visualizes product-wise and time-based sales performance.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/02. Simple Sales Report/data.csv')

print("Original Data:")
print(df, "\n")

df["Quantity"].fillna(0, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df["Revenue"] = df["Quantity"] * df["Price"]

print("After Cleaning & Revenue Calculation:")
print(df, "\n")

product_sales = df.groupby("Product")["Revenue"].sum().reset_index()
region_sales = df.groupby("Region")["Revenue"].sum().reset_index()
daily_sales = df.groupby("Date")["Revenue"].sum().reset_index()

best_product = product_sales.loc[product_sales["Revenue"].idxmax(), "Product"]

print("Product-wise Sales:")
print(product_sales, "\n")

print("Region-wise Sales:")
print(region_sales, "\n")

print("Best Selling Product:", best_product)

# =========================
# 📊 SEABORN VISUALS
# =========================

sns.set_style("whitegrid")

# 1️⃣ Bar Plot: Product-wise Revenue
plt.figure(figsize=(8, 5))
sns.barplot(data=product_sales, x="Product", y="Revenue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# 2️⃣ Line Plot: Revenue Over Time
plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_sales, x="Date", y="Revenue", marker="o")
plt.title("Sales Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()