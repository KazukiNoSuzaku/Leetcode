# Author: Kaustav Ghosh
# Problem: League Statistics (Premium)
# Approach: Expand each match into two team rows (home and away) carrying points/scored/conceded, aggregate per team, then order by points desc then name asc

import pandas as pd

def league_statistics(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    def points(gf, ga):
        return (gf > ga) * 3 + (gf == ga) * 1

    home = pd.DataFrame({
        'team_id': matches['home_team_id'],
        'played': 1,
        'points': [points(f, a) for f, a in zip(matches['home_team_goals'], matches['away_team_goals'])],
        'scored': matches['home_team_goals'],
        'conceded': matches['away_team_goals'],
    })
    away = pd.DataFrame({
        'team_id': matches['away_team_id'],
        'played': 1,
        'points': [points(f, a) for f, a in zip(matches['away_team_goals'], matches['home_team_goals'])],
        'scored': matches['away_team_goals'],
        'conceded': matches['home_team_goals'],
    })

    agg = pd.concat([home, away]).groupby('team_id', as_index=False).sum()
    df = agg.merge(teams, on='team_id')
    df['matches_played'] = df['played']
    df['goal_for'] = df['scored']
    df['goal_against'] = df['conceded']
    df['goal_diff'] = df['scored'] - df['conceded']
    df = df.sort_values(['points', 'goal_diff', 'team_name'], ascending=[False, False, True])
    return df[['team_name', 'matches_played', 'points', 'goal_for', 'goal_against', 'goal_diff']]
