# This project analyzes stock market data using Pandas.
# It calculates moving averages, identifies top gainers and losers,
# and performs company-wise trend analysis.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/10. Stock Market Data Analysis/data.csv')

print("Original Data:")
print(df)
print("\n")

df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(["Company", "Date"], inplace=True)

df["MA_2"] = df.groupby("Company")["Close"].transform(lambda x: x.rolling(2).mean())

company_max_close = df.groupby("Company")["Close"].max()
company_min_close = df.groupby("Company")["Close"].min()

df["DailyChange"] = df["Close"] - df["Open"]
top_gainers = df.loc[df.groupby("Date")["DailyChange"].idxmax()]

print("Stock Data with 2-day Moving Average:")
print(df)
print("\n")

print("Company-wise Highest Closing Price:")
print(company_max_close)
print("\n")

print("Company-wise Lowest Closing Price:")
print(company_min_close)
print("\n")

print("Top Gainers Each Day:")
print(top_gainers)
