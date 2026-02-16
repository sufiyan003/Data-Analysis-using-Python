# This project generates random numerical data using NumPy.
# It calculates basic statistics such as mean, median, std, min, max,
# and filters values based on specified conditions.

import numpy as np

data = np.random.randint(1, 101, size=20)

mean = np.mean(data)
median = np.median(data)
std = np.std(data)
min_val = np.min(data)
max_val = np.max(data)

above_mean = data[data > mean]

below_mean = data[data < mean]

print("Random Data:", data)
print(f"Mean: {mean}, Median: {median}, Std: {std:.2f}")
print(f"Min: {min_val}, Max: {max_val}")
print("Values Above Mean:", above_mean)
print("Values Below Mean:", below_mean)
