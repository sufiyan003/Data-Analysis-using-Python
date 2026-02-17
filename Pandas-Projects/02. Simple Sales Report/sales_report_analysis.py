# This project analyzes sales data using Pandas.
# It calculates revenue, handles missing values,
# and generates product-wise and region-wise sales reports.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/02. Simple Sales Report/data.csv')

print("Original Data:")
print(df)
print("\n")

df["Quantity"].fillna(0, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df["Revenue"] = df["Quantity"] * df["Price"]

print("After Cleaning & Revenue Calculation:")
print(df)
print("\n")

product_sales = df.groupby("Product")["Revenue"].sum()

region_sales = df.groupby("Region")["Revenue"].sum()

best_product = product_sales.idxmax()

print("Product-wise Sales:")
print(product_sales)
print("\n")

print("Region-wise Sales:")
print(region_sales)
print("\n")

print("Best Selling Product:", best_product)
