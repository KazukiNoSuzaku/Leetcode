# Author: Kaustav Ghosh
# Problem: Leetcodify Friends Recommendations
# Approach: Self-join distinct listens on (song, day) to find user pairs who heard the same song the same day, then keep pairs sharing at least three unique songs on some day. Drop pairs that are already friends (either direction) and return both directions deduplicated

import pandas as pd

def recommend_friends(listens: pd.DataFrame, friendship: pd.DataFrame) -> pd.DataFrame:
    plays = listens[['user_id', 'song_id', 'day']].drop_duplicates()
    paired = plays.merge(plays, on=['song_id', 'day'])
    paired = paired[paired['user_id_x'] != paired['user_id_y']]

    shared = (paired.groupby(['user_id_x', 'user_id_y', 'day'])['song_id']
              .nunique()
              .reset_index())
    pairs = shared[shared['song_id'] >= 3][['user_id_x', 'user_id_y']].drop_duplicates()

    fwd = friendship.rename(columns={'user1_id': 'a', 'user2_id': 'b'})[['a', 'b']]
    bwd = friendship.rename(columns={'user1_id': 'b', 'user2_id': 'a'})[['a', 'b']]
    friend_pairs = set(zip(pd.concat([fwd, bwd])['a'], pd.concat([fwd, bwd])['b']))

    keep = [(x, y) not in friend_pairs
            for x, y in zip(pairs['user_id_x'], pairs['user_id_y'])]
    result = pairs[keep].rename(columns={'user_id_x': 'user_id',
                                         'user_id_y': 'recommended_id'})
    return result.drop_duplicates()
