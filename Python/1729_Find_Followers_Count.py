# Author: Kaustav Ghosh
# Problem: Find Followers Count
# Approach: Count distinct followers per user and order by user id

import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    result = followers.groupby('user_id', as_index=False)['follower_id'].nunique()
    result = result.rename(columns={'follower_id': 'followers_count'})
    return result.sort_values('user_id')
