# This project simulates a mini data analysis dashboard using NumPy arrays.
# It combines multiple datasets (sales, inventory, profit),
# calculates aggregated statistics, and filters best/worst performing items.

import numpy as np

sales = np.array([
    [1200, 1500, 1700],  
    [900, 1100, 1300],  
    [600,  800,  900]   
])

inventory = np.array([
    [50, 40, 30], 
    [30, 25, 20],  
    [20, 15, 10]  
])

profit = np.array([
    [300, 400, 500], 
    [100, 150, 200], 
    [50,  70,  80]  
])

total_sales = np.sum(sales, axis=1)
total_inventory = np.sum(inventory, axis=1)
total_profit = np.sum(profit, axis=1)

monthly_avg_sales = np.mean(sales, axis=0)

best_selling_index = np.argmax(total_sales)

high_profit_products = np.where(total_profit > 400)[0]  

print("Total Sales per Product:", total_sales)
print("Total Inventory per Product:", total_inventory)
print("Total Profit per Product:", total_profit)
print("Monthly Average Sales:", monthly_avg_sales)
print(f"Best Selling Product: Product {best_selling_index + 1}")
print("High Profit Products (indices):", high_profit_products)
