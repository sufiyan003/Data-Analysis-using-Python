# This project analyzes e-commerce order data using Pandas and Seaborn.
# It calculates revenue per product, identifies top customers,
# and visualizes product-wise revenue using a bar chart.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/05. E-commerce Order Analysis/data.csv')

print("Original Data:")
print(df, "\n")

df["Quantity"].fillna(0, inplace=True)
df["Price"].fillna(0, inplace=True)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

df["Revenue"] = df["Quantity"] * df["Price"]

product_revenue = df.groupby("Product")["Revenue"].sum().reset_index()
customer_revenue = df.groupby("Customer")["Revenue"].sum().reset_index()
df["Month"] = df["OrderDate"].dt.month
monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()

most_ordered_product = df.groupby("Product")["Quantity"].sum().idxmax()

print("Product-wise Revenue:")
print(product_revenue, "\n")

print("Customer-wise Revenue:")
print(customer_revenue, "\n")

print("Monthly Revenue:")
print(monthly_revenue, "\n")

print("Most Ordered Product:", most_ordered_product)

# =========================
# 📊 SEABORN VISUAL
# =========================

sns.set_style("whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(data=product_revenue, x="Product", y="Revenue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()