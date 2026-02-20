# This project segments customers based on spending using Pandas and Matplotlib.
# It categorizes customers into low, medium, and high spenders,
# calculates segment-wise total revenue, and visualizes segments using a pie chart.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/06. Customer Segmentation/data.csv')

print("Original Data:")
print(df, "\n")

bins = [0, 50000, 100000, float("inf")]
labels = ["Low Spender", "Medium Spender", "High Spender"]
df["Segment"] = pd.cut(df["TotalSpend"], bins=bins, labels=labels)

segment_revenue = df.groupby("Segment")["TotalSpend"].sum()
segment_avg_orders = df.groupby("Segment")["Orders"].mean()

top_high_spenders = df[df["Segment"] == "High Spender"].sort_values("TotalSpend", ascending=False)

print("Segment-wise Total Spend:")
print(segment_revenue, "\n")

print("Segment-wise Average Orders:")
print(segment_avg_orders, "\n")

print("Top High Spenders:")
print(top_high_spenders, "\n")

# =========================
# 📊 MATPLOTLIB VISUAL
# =========================

plt.figure()
segment_revenue.plot(kind="pie", autopct="%1.1f%%", startangle=140)
plt.title("Customer Segmentation by Total Spend")
plt.ylabel("") 
plt.show()