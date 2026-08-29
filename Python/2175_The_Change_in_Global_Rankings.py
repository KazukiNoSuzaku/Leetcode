# Author: Kaustav Ghosh
# Problem: The Change in Global Rankings
# Approach: Rank teams by points descending, breaking ties by name ascending, before and after applying each team's points change. The rank change is the old rank minus the new rank

import pandas as pd

def get_global_ranking(teams: pd.DataFrame, points_change: pd.DataFrame) -> pd.DataFrame:
    df = teams.merge(points_change, on='team_id')
    df['new_points'] = df['points'] + df['points_change']

    df = df.sort_values(['points', 'name'], ascending=[False, True]).reset_index(drop=True)
    df['old_rank'] = df.index + 1

    df = df.sort_values(['new_points', 'name'], ascending=[False, True]).reset_index(drop=True)
    df['new_rank'] = df.index + 1

    df['rank_change'] = df['old_rank'] - df['new_rank']
    return df[['team_id', 'name', 'rank_change']]
