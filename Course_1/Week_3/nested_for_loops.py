"""
This script is used for course notes.

Author: Erick Marin
Date: 10/10/2020
"""

for left in range(7):   # loop iterates 6 times
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

teams = ["Dragons", "Wolves", "Panda", "Unicorns"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
