# Author: Kaustav Ghosh
# Problem: Strong Friendship
# Approach: Expand friendships into a bidirectional (person, friend) table. For each original edge, join to find friends of user1 that are also friends of user2 - those are common friends. A friendship is strong when it has at least three common friends

import pandas as pd

def strong_friendship(friendship: pd.DataFrame) -> pd.DataFrame:
    a = friendship.rename(columns={'user1_id': 'person', 'user2_id': 'friend'})[['person', 'friend']]
    b = friendship.rename(columns={'user1_id': 'friend', 'user2_id': 'person'})[['person', 'friend']]
    bi = pd.concat([a, b], ignore_index=True)

    edges = friendship[['user1_id', 'user2_id']]
    m1 = edges.merge(bi, left_on='user1_id', right_on='person')     # friend of user1
    res = m1.merge(bi, left_on=['user2_id', 'friend'],
                   right_on=['person', 'friend'])                    # also friend of user2

    res = res[(res['friend'] != res['user1_id']) & (res['friend'] != res['user2_id'])]

    grp = (res.groupby(['user1_id', 'user2_id'])
           .size()
           .reset_index(name='common_friend'))
    return grp[grp['common_friend'] >= 3]
