# This project analyzes financial transactions using Pandas.
# It calculates daily and monthly expenses, identifies high-risk transactions,
# and provides account-wise transaction summaries.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/08. Financial Transactions Analyzer/data.csv')

print("Original Data:")
print(df)
print("\n")

df["Date"] = pd.to_datetime(df["Date"])

daily_expenses = df[df["TransactionType"] == "Debit"].groupby("Date")["Amount"].sum()

df["Month"] = df["Date"].dt.month
monthly_expenses = df[df["TransactionType"] == "Debit"].groupby("Month")["Amount"].sum()

account_summary = df.groupby("AccountHolder")["Amount"].sum()

high_risk = df[df["Amount"] > 10000]

print("Daily Expenses:")
print(daily_expenses)
print("\n")

print("Monthly Expenses:")
print(monthly_expenses)
print("\n")

print("Account-wise Total Transactions:")
print(account_summary)
print("\n")

print("High-Risk Transactions (>10000):")
print(high_risk)
