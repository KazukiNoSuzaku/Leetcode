# Author: Kaustav Ghosh
# Problem: Users That Actively Request Confirmation Messages
# Approach: Sort each user's request timestamps and compare consecutive ones; a user qualifies if two of their requests fall within 24 hours (<= 86400 seconds) of each other

import pandas as pd

def active_users(confirmations: pd.DataFrame) -> pd.DataFrame:
    df = confirmations.copy()
    df['time_stamp'] = pd.to_datetime(df['time_stamp'])
    df = df.sort_values(['user_id', 'time_stamp'])
    df['prev'] = df.groupby('user_id')['time_stamp'].shift(1)
    gap = (df['time_stamp'] - df['prev']).dt.total_seconds()
    users = df.loc[gap <= 24 * 3600, 'user_id'].unique()
    return pd.DataFrame({'user_id': users})
