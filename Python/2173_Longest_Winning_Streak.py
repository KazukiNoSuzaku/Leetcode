# Author: Kaustav Ghosh
# Problem: Longest Winning Streak
# Approach: For each player, scan matches in day order and track the longest run of consecutive wins, resetting the current run on any non-win

import pandas as pd

def longest_winning_streak(matches: pd.DataFrame) -> pd.DataFrame:
    ordered = matches.sort_values(['player_id', 'match_day'])
    rows = []
    for player_id, group in ordered.groupby('player_id'):
        best = current = 0
        for result in group['result']:
            if result == 'Win':
                current += 1
                best = max(best, current)
            else:
                current = 0
        rows.append((player_id, best))
    return pd.DataFrame(rows, columns=['player_id', 'longest_streak'])
