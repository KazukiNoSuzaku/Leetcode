# Author: Kaustav Ghosh
# Problem: The Latest Login in 2020
# Approach: Keep only 2020 logins and, per user, report the maximum timestamp

import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    df = logins.copy()
    df['time_stamp'] = pd.to_datetime(df['time_stamp'])
    df = df[df['time_stamp'].dt.year == 2020]
    result = df.groupby('user_id', as_index=False)['time_stamp'].max()
    return result.rename(columns={'time_stamp': 'last_stamp'})
