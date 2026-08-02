# Author: Kaustav Ghosh
# Problem: Page Recommendations II (Premium)
# Approach: Expand friendships both ways, join each user's friends' liked pages, drop pages the user already likes, then count distinct friends who liked each recommended page

import pandas as pd

def recommend_page(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:
    friends = pd.concat([
        friendship.rename(columns={'user1_id': 'user_id', 'user2_id': 'friend_id'}),
        friendship.rename(columns={'user2_id': 'user_id', 'user1_id': 'friend_id'}),
    ])

    # pages each friend likes
    friend_pages = friends.merge(likes, left_on='friend_id', right_on='user_id',
                                 suffixes=('', '_f'))[['user_id', 'friend_id', 'page_id']]

    # remove pages the user already likes
    own = likes.rename(columns={'user_id': 'user_id'})
    merged = friend_pages.merge(own, on=['user_id', 'page_id'], how='left', indicator=True)
    recommend = merged[merged['_merge'] == 'left_only']

    result = recommend.groupby(['user_id', 'page_id'], as_index=False)['friend_id'].nunique()
    return result.rename(columns={'friend_id': 'friends_likes'})
