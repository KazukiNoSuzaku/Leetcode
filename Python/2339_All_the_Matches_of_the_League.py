# Author: Kaustav Ghosh
# Problem: All the Matches of the League
# Approach: Every pair of teams plays twice, each side hosting once, so cross join the teams table with itself, drop the rows pairing a team with itself, and label the two sides home_team and away_team

import pandas as pd


def league(teams: pd.DataFrame) -> pd.DataFrame:
    matches = teams.merge(teams, how="cross", suffixes=("_home", "_away"))
    matches = matches[matches["team_name_home"] != matches["team_name_away"]]
    matches = matches.rename(columns={"team_name_home": "home_team", "team_name_away": "away_team"})
    return matches[["home_team", "away_team"]].reset_index(drop=True)
