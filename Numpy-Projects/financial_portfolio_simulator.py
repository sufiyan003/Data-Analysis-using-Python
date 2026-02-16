# This project simulates a financial portfolio using NumPy arrays.
# It calculates daily returns, total returns, identifies profitable days,
# and filters stocks based on performance thresholds.

import numpy as np

prices = np.array([
    [100, 102, 101, 105, 110], 
    [50, 48, 49, 51, 52],     
    [200, 198, 202, 205, 210]  
])

daily_returns = (prices[:, 1:] - prices[:, :-1]) / prices[:, :-1]

total_returns = prices[:, -1] - prices[:, 0]

profitable_days = daily_returns > 0

top_stocks = np.where(total_returns > 5)[0] 

print("Stock Prices:\n", prices)
print("\nDaily Returns:\n", daily_returns)
print("\nTotal Returns per Stock:", total_returns)
print("\nProfitable Days (True = positive return):\n", profitable_days)
print("Top Stocks (total return > 5, indices):", top_stocks)
