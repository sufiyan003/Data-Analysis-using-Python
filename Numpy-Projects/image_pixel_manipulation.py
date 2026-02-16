# This project simulates image pixel manipulation using NumPy arrays.
# It demonstrates operations like brightening, darkening, inverting colors,
# and cropping parts of an image represented as a 3D array (Height x Width x RGB).

import numpy as np

np.random.seed(42)
image = np.random.randint(0, 256, size=(4, 4, 3))

bright_image = np.clip(image + 50, 0, 255)

dark_image = np.clip(image - 50, 0, 255)

inverted_image = 255 - image

cropped_image = image[:2, :2, :]

print("Original Image (4x4 RGB):\n", image)
print("\nBrightened Image:\n", bright_image)
print("\nDarkened Image:\n", dark_image)
print("\nInverted Image:\n", inverted_image)
print("\nCropped Image (2x2 top-left):\n", cropped_image)
