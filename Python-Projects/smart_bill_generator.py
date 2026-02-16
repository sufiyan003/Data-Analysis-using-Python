"""
Project: Smart Bill Generator
Goal: Practice using 'while' loops for continuous user input and 
      dynamic lists to store, calculate, and display itemized data.
"""

items = []
prices = []

while True:
    item = input("Enter item name (or 'done' to finish): ")
    
    if item.lower() == 'done':
        break
    
    price = float(input(f"Enter price for {item}: "))
    
    items.append(item)
    prices.append(price)

print("\n--- FINAL BILL ---")
for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]}")

print(f"Total: ${sum(prices)}")