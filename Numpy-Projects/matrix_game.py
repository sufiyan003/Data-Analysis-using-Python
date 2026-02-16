# This project simulates multiple game boards using NumPy 3D arrays.
# It calculates wins per player across multiple games,
# identifies top performing boards, and demonstrates broadcasting and aggregation.

import numpy as np

np.random.seed(42) 
games = np.random.randint(0, 11, size=(3, 4, 5))

total_scores = np.sum(games, axis=2)

winners = np.argmax(total_scores, axis=1)

overall_scores = np.sum(total_scores, axis=0)
overall_top_player = np.argmax(overall_scores)

print("Games Scores (3D array):\n", games)
print("\nTotal Scores per Player per Game:\n", total_scores)
print("Winners per Game (player index):", winners)
print("Overall Top Player (player index):", overall_top_player)
