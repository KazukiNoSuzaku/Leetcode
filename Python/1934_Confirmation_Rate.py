# Author: Kaustav Ghosh
# Problem: Confirmation Rate
# Approach: A user's confirmation rate is the fraction of their confirmation requests with action 'confirmed'. Compute the mean of a confirmed indicator per user, map it onto every signed-up user, and default users with no requests to 0

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    conf = confirmations.copy()
    conf['is_confirmed'] = (conf['action'] == 'confirmed').astype(float)
    rate = conf.groupby('user_id')['is_confirmed'].mean()

    result = signups[['user_id']].copy()
    result['confirmation_rate'] = result['user_id'].map(rate).fillna(0).round(2)
    return result
