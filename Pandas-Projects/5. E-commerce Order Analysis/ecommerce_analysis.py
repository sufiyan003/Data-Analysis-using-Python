# This project analyzes e-commerce order data using Pandas.
# It calculates revenue per product, top customers, and monthly sales trends.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/5. E-commerce Order Analysis/data.csv')

print("Original Data:")
print(df)
print("\n")

df["Quantity"].fillna(0, inplace=True)
df["Price"].fillna(0, inplace=True)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

df["Revenue"] = df["Quantity"] * df["Price"]

product_revenue = df.groupby("Product")["Revenue"].sum()

customer_revenue = df.groupby("Customer")["Revenue"].sum()

df["Month"] = df["OrderDate"].dt.month
monthly_revenue = df.groupby("Month")["Revenue"].sum()

most_ordered_product = df.groupby("Product")["Quantity"].sum().idxmax()

print("Product-wise Revenue:")
print(product_revenue)
print("\n")

print("Customer-wise Revenue:")
print(customer_revenue)
print("\n")

print("Monthly Revenue:")
print(monthly_revenue)
print("\n")

print("Most Ordered Product:", most_ordered_product)
