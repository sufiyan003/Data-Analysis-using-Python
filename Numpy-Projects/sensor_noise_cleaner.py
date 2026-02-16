# This project cleans noisy sensor data using NumPy.
# It detects and removes outliers based on statistical thresholds
# to produce more reliable and accurate sensor readings.

import numpy as np

sensor_data = np.array([22, 23, 100, 24, 25, 102, 23, 24])

mean = np.mean(sensor_data)
std = np.std(sensor_data)

clean_data = sensor_data[(sensor_data > mean - 2*std) & (sensor_data < mean + 2*std)]

print("Original Sensor Data:", sensor_data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Cleaned Sensor Data:", clean_data)
