"""
Project: Player Performance Analyzer
Goal: Demonstrates the use of Dictionaries to store nested data (lists) 
      and loops to calculate numerical averages for data analysis.
"""

players = {
    "Camilla": [10, 12, 8, 15],
    "John": [5, 7, 6, 4],
    "Ryan": [20, 18, 22, 25]
}

for name, goals in players.items():
    avg_goals = sum(goals) / len(goals)
    print(f"{name}'s Average Goals: {avg_goals}")