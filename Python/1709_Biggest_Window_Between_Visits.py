# Author: Kaustav Ghosh
# Problem: Biggest Window Between Visits (Premium)
# Approach: Per user, sort visits and diff each with the next (the last visit uses 2021-01-01), then take the largest gap in days

import pandas as pd

def biggest_window_between_visits(user_visits: pd.DataFrame) -> pd.DataFrame:
    df = user_visits.copy()
    df['visit_date'] = pd.to_datetime(df['visit_date'])
    df = df.sort_values(['user_id', 'visit_date'])
    df['next_date'] = df.groupby('user_id')['visit_date'].shift(-1)
    df['next_date'] = df['next_date'].fillna(pd.Timestamp('2021-01-01'))
    df['window'] = (df['next_date'] - df['visit_date']).dt.days
    result = df.groupby('user_id', as_index=False)['window'].max()
    return result.rename(columns={'window': 'biggest_window'}).sort_values('user_id')
