# This project performs sales data analysis using NumPy arrays.
# It calculates total and average sales, applies bonuses using broadcasting,
# and filters high sales values for business insights.

import numpy as np

sales = np.array([
    [1200, 1500, 1700, 1600, 1800, 2000],  
    [900, 1100, 1300, 1250, 1400, 1500],  
    [600,  800,  900,  950, 1000, 1200]  
])

total_sales = np.sum(sales, axis=1)

monthly_avg = np.mean(sales, axis=0)

bonus_sales = sales * 1.10

high_sales = sales[sales > 1500]

print("Total Sales per Product:", total_sales)
print("Monthly Average Sales:", monthly_avg)
print("Sales after 10% Bonus:\n", bonus_sales)
print("High Sales Values (>1500):", high_sales)
