# This project analyzes COVID-19 data using Pandas and Matplotlib.
# It handles missing values, calculates death and recovery rates,
# performs country-wise aggregation, and visualizes trends over time.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Matplotlib-Projects/07. COVID & Health Data Analysis/data.csv')

print("Original Data:")
print(df, "\n")

df["Confirmed"] = df["Confirmed"].ffill() 
df["Deaths"].fillna(0, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df["DeathRate"] = (df["Deaths"] / df["Confirmed"]) * 100
df["RecoveryRate"] = (df["Recovered"] / df["Confirmed"]) * 100

country_cases = df.groupby("Country")["Confirmed"].sum()
country_death_rate = df.groupby("Country")["DeathRate"].mean()
high_risk_countries = country_death_rate[country_death_rate > 5]

print("Country-wise Total Confirmed Cases:")
print(country_cases, "\n")

print("Country-wise Average Death Rate:")
print(country_death_rate, "\n")

print("High-Risk Countries (Death Rate > 5%):")
print(high_risk_countries, "\n")

# =========================
# 📊 MATPLOTLIB VISUALS
# =========================

# Line chart: Confirmed cases over time
plt.figure()
df.groupby("Date")["Confirmed"].sum().plot(kind="line")
plt.title("Daily Confirmed COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.show()

# Line chart: Deaths over time
plt.figure()
df.groupby("Date")["Deaths"].sum().plot(kind="line", color="red")
plt.title("Daily COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.show()