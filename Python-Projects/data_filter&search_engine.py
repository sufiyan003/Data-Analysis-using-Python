"""
Project: Data Filter & Search Engine
Goal: To simulate database filtering logic using Python lists and loops. 
      This mimics how data is filtered in SQL or Pandas.
"""

data = [
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Grocery", "price": 2},
    {"name": "Phone", "category": "Electronics", "price": 800},
    {"name": "Apple", "category": "Grocery", "price": 1},
    {"name": "Headphones", "category": "Electronics", "price": 150}
]

search_category = "Electronics"
filtered_results = []

for item in data:
    if item["category"] == search_category:
        filtered_results.append(item)

print(f"--- Items in {search_category} ---")
for result in filtered_results:
    print(f"Product: {result['name']} | Price: ${result['price']}")

total_value = sum(item["price"] for item in filtered_results)
print(f"\nTotal Value of {search_category}: ${total_value}")