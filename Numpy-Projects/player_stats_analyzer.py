# This project analyzes players' performance stats using NumPy arrays.
# It calculates average, maximum, and minimum scores per player,
# identifies top performers, and filters players based on performance thresholds.

import numpy as np

player_scores = np.array([
    [10, 15, 12, 20], 
    [8, 9, 7, 10],   
    [14, 18, 20, 22], 
    [5, 6, 4, 7],     
    [12, 14, 13, 15]  
])

player_avg = np.mean(player_scores, axis=1)

player_max = np.max(player_scores, axis=1)

player_min = np.min(player_scores, axis=1)

top_player_index = np.argmax(player_avg)
top_player_score = player_avg[top_player_index]

high_performers = player_scores[player_avg >= 15]

print("Average Scores per Player:", player_avg)
print("Max Scores per Player:", player_max)
print("Min Scores per Player:", player_min)
print(f"Top Player: Player {top_player_index + 1} with average {top_player_score}")
print("High Performing Players (avg >= 15):\n", high_performers)
