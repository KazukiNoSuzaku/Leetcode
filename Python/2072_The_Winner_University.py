# Author: Kaustav Ghosh
# Problem: The Winner University
# Approach: Count excellent students (score >= 90) at each university and compare; the larger count wins, otherwise it is a tie

import pandas as pd

def find_winner(newyork: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    ny = int((newyork['score'] >= 90).sum())
    ca = int((california['score'] >= 90).sum())
    if ny > ca:
        winner = 'New York University'
    elif ca > ny:
        winner = 'California University'
    else:
        winner = 'No Winner'
    return pd.DataFrame({'winner': [winner]})
