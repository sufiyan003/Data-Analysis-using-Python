# This project segments customers based on their spending using Pandas.
# It categorizes customers into low, medium, and high spenders
# and calculates segment-wise total revenue and average orders.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/06. Customer Segmentation/data.csv')

print("Original Data:")
print(df)
print("\n")

bins = [0, 50000, 100000, float("inf")]
labels = ["Low Spender", "Medium Spender", "High Spender"]
df["Segment"] = pd.cut(df["TotalSpend"], bins=bins, labels=labels)

segment_revenue = df.groupby("Segment")["TotalSpend"].sum()

segment_avg_orders = df.groupby("Segment")["Orders"].mean()

top_high_spenders = df[df["Segment"] == "High Spender"].sort_values("TotalSpend", ascending=False)

print("Segment-wise Total Spend:")
print(segment_revenue)
print("\n")

print("Segment-wise Average Orders:")
print(segment_avg_orders)
print("\n")

print("Top High Spenders:")
print(top_high_spenders)
