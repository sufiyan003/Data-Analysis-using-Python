# This project analyzes financial transactions using Pandas and Matplotlib.
# It calculates daily and monthly expenses, identifies high-risk transactions,
# and visualizes account-wise summaries and daily expense trends.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/08. Financial Transactions Analyzer/data.csv')

print("Original Data:")
print(df, "\n")

df["Date"] = pd.to_datetime(df["Date"])

daily_expenses = df[df["TransactionType"] == "Debit"].groupby("Date")["Amount"].sum()

df["Month"] = df["Date"].dt.month
monthly_expenses = df[df["TransactionType"] == "Debit"].groupby("Month")["Amount"].sum()

account_summary = df.groupby("AccountHolder")["Amount"].sum()

high_risk = df[df["Amount"] > 10000]

print("Daily Expenses:")
print(daily_expenses, "\n")

print("Monthly Expenses:")
print(monthly_expenses, "\n")

print("Account-wise Total Transactions:")
print(account_summary, "\n")

print("High-Risk Transactions (>10000):")
print(high_risk, "\n")

# =========================
# 📊 MATPLOTLIB VISUALS
# =========================

# 1️⃣ Pie Chart: Account-wise Total Transactions
plt.figure()
account_summary.plot(kind="pie", autopct="%1.1f%%", startangle=140)
plt.title("Account-wise Total Transactions")
plt.ylabel("")
plt.show()

# 2️⃣ Line Chart: Daily Expenses Trend
plt.figure()
daily_expenses.plot(kind="line", color="green")
plt.title("Daily Expenses Over Time")
plt.xlabel("Date")
plt.ylabel("Expense Amount")
plt.xticks(rotation=45)
plt.show()