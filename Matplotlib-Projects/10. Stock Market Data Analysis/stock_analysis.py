# This project analyzes stock market data using Pandas and Matplotlib.
# It calculates moving averages, identifies top gainers and losers,
# and visualizes company-wise closing price trends with moving averages.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/10. Stock Market Data Analysis/data.csv')

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
# 📊 MATPLOTLIB VISUALS
# =========================

companies = df["Company"].unique()

plt.figure(figsize=(10,6))

for company in companies:
    company_data = df[df["Company"] == company]
    plt.plot(company_data["Date"], company_data["Close"], label=f"{company} Close")
    plt.plot(company_data["Date"], company_data["MA_2"], linestyle="--", label=f"{company} MA-2")

plt.title("Stock Closing Prices with 2-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.xticks(rotation=45)
plt.show()