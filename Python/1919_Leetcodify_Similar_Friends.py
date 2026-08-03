# Author: Kaustav Ghosh
# Problem: Leetcodify Similar Friends
# Approach: For each friend pair, join user1's distinct listens to user2's on (song, day) so only songs both heard the same day survive, then keep pairs that share three or more unique songs on some day

import pandas as pd

def similar_friends(friendship: pd.DataFrame, listens: pd.DataFrame) -> pd.DataFrame:
    plays = listens[['user_id', 'song_id', 'day']].drop_duplicates()

    step = friendship.merge(plays, left_on='user1_id', right_on='user_id')
    step = step[['user1_id', 'user2_id', 'song_id', 'day']]

    both = step.merge(plays, left_on=['user2_id', 'song_id', 'day'],
                      right_on=['user_id', 'song_id', 'day'])
    both = both[['user1_id', 'user2_id', 'song_id', 'day']]

    counts = (both.groupby(['user1_id', 'user2_id', 'day'])['song_id']
              .nunique()
              .reset_index())
    return counts[counts['song_id'] >= 3][['user1_id', 'user2_id']].drop_duplicates()
