# This project analyzes COVID-19 data using Pandas.
# It handles missing values, calculates death and recovery rates,
# performs country-wise aggregation, and identifies high-risk countries.

import pandas as pd

df = pd.read_csv('C:/Users/hp/Data-Analysis-using-Python/Pandas-Projects/7. COVID & Health Data Analysis/data.csv')

print("Original Data:")
print(df)
print("\n")

df["Confirmed"] = df["Confirmed"].ffill() 
df["Deaths"].fillna(0, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df["DeathRate"] = (df["Deaths"] / df["Confirmed"]) * 100
df["RecoveryRate"] = (df["Recovered"] / df["Confirmed"]) * 100

country_cases = df.groupby("Country")["Confirmed"].sum()

country_death_rate = df.groupby("Country")["DeathRate"].mean()

high_risk_countries = country_death_rate[country_death_rate > 5]

print("Country-wise Total Confirmed Cases:")
print(country_cases)
print("\n")

print("Country-wise Average Death Rate:")
print(country_death_rate)
print("\n")

print("High-Risk Countries (Death Rate > 5%):")
print(high_risk_countries)
