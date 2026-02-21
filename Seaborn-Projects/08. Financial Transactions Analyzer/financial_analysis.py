# This project analyzes financial transactions using Pandas and Seaborn.
# It calculates daily and monthly expenses, identifies high-risk transactions,
# and visualizes account-wise summaries and daily expense trends.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Seaborn-Projects/08. Financial Transactions Analyzer/data.csv')

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
# 📊 SEABORN VISUALS
# =========================

sns.set_style("whitegrid")

# 1️⃣ Boxplot: Transaction Amounts per Account
plt.figure(figsize=(10, 5))
sns.boxplot(x="AccountHolder", y="Amount", data=df)
plt.title("Transaction Amounts per Account")
plt.xlabel("Account Holder")
plt.ylabel("Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2️⃣ Lineplot: Daily Expenses Trend
daily_expenses_reset = daily_expenses.reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_expenses_reset, x="Date", y="Amount", color="green")
plt.title("Daily Expenses Over Time")
plt.xlabel("Date")
plt.ylabel("Expense Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()