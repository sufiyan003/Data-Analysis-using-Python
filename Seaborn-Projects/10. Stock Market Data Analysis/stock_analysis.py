# This project analyzes stock market data using Pandas and Seaborn.
# It calculates moving averages, identifies top gainers and losers,
# and visualizes company-wise closing price trends with moving averages using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/10. Stock Market Data Analysis/data.csv')

print("Original Data:")
print(df, "\n")

df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(["Company", "Date"], inplace=True)

df["MA_2"] = df.groupby("Company")["Close"].transform(lambda x: x.rolling(2).mean())

company_max_close = df.groupby("Company")["Close"].max()
company_min_close = df.groupby("Company")["Close"].min()

df["DailyChange"] = df["Close"] - df["Open"]
top_gainers = df.loc[df.groupby("Date")["DailyChange"].idxmax()]

print("Stock Data with 2-day Moving Average:")
print(df, "\n")

print("Company-wise Highest Closing Price:")
print(company_max_close, "\n")

print("Company-wise Lowest Closing Price:")
print(company_min_close, "\n")

print("Top Gainers Each Day:")
print(top_gainers, "\n")

# =========================
# 📊 SEABORN VISUAL
# =========================

sns.set_style("whitegrid")
plt.figure(figsize=(12,6))

companies = df["Company"].unique()

for company in companies:
    company_data = df[df["Company"] == company]
    sns.lineplot(x="Date", y="Close", data=company_data, label=f"{company} Close")
    sns.lineplot(x="Date", y="MA_2", data=company_data, linestyle="--", label=f"{company} MA-2")

plt.title("Stock Closing Prices with 2-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()