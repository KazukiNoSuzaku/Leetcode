# Author: Kaustav Ghosh
# Problem: Grand Slam Titles (Premium)
# Approach: Melt the four championship columns into one player-id series, tally wins per player, and join their names

import pandas as pd

def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:
    winners = pd.concat([
        championships['Wimbledon'],
        championships['Fr_open'],
        championships['US_open'],
        championships['Au_open'],
    ])
    counts = winners.value_counts().reset_index()
    counts.columns = ['player_id', 'grand_slams_count']
    result = counts.merge(players, on='player_id')
    return result[['player_id', 'player_name', 'grand_slams_count']]
