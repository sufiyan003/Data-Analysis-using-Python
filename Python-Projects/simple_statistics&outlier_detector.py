"""
Project: Simple Statistics & Outlier Detector
Goal: To manually calculate Mean (Average) and detect Outliers in a dataset. 
      Fundamental logic for data cleaning in Data Science.
"""

dataset = [10, 12, 11, 15, 13, 100, 14, 12, 11] 

mean_value = sum(dataset) / len(dataset)

outliers = []
clean_data = []

for value in dataset:
    if value > (mean_value * 2):
        outliers.append(value)
    else:
        clean_data.append(value)

print(f"Dataset: {dataset}")
print(f"Average: {mean_value:.2f}")
print(f"Detected Outliers: {outliers}")
print(f"Cleaned Data: {clean_data}")