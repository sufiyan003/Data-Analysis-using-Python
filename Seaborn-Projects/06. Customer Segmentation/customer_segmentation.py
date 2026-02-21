# This project segments customers based on spending using Pandas and Seaborn.
# It categorizes customers into low, medium, and high spenders,
# calculates segment-wise total revenue, and visualizes segments with count and box plots.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/06. Customer Segmentation/data.csv')

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
# 📊 SEABORN VISUALS
# =========================

sns.set_style("whitegrid")

# 1️⃣ Count Plot: Number of Customers per Segment
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Segment", order=labels)
plt.title("Customer Count per Segment")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 2️⃣ Box Plot: Spending Distribution per Segment
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Segment", y="TotalSpend", order=labels)
plt.title("Spending Distribution per Segment")
plt.xlabel("Segment")
plt.ylabel("Total Spend")
plt.tight_layout()
plt.show()

# 3️⃣ Optional Pie Chart: Segment Revenue Share (Matplotlib)
plt.figure(figsize=(6, 6))
plt.pie(segment_revenue, labels=segment_revenue.index, autopct="%1.1f%%", startangle=140)
plt.title("Customer Segmentation by Total Spend")
plt.tight_layout()
plt.show()