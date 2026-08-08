# Author: Kaustav Ghosh
# Problem: All the Pairs With the Maximum Number of Common Followers
# Approach: Self-join the relations on follower_id so each row pairs two users sharing a follower (user1 < user2), count shared followers per pair, and return the pairs whose count equals the maximum

import pandas as pd

def count_pairs(relations: pd.DataFrame) -> pd.DataFrame:
    m = relations.merge(relations, on='follower_id')
    m = m[m['user_id_x'] < m['user_id_y']]

    grp = (m.groupby(['user_id_x', 'user_id_y'])
           .size()
           .reset_index(name='cnt'))
    if grp.empty:
        return pd.DataFrame(columns=['user1_id', 'user2_id'])

    top = grp[grp['cnt'] == grp['cnt'].max()]
    return top[['user_id_x', 'user_id_y']].rename(
        columns={'user_id_x': 'user1_id', 'user_id_y': 'user2_id'})
