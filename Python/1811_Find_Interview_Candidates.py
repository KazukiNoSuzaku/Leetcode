# Author: Kaustav Ghosh
# Problem: Find Interview Candidates (Premium)
# Approach: A candidate either won a medal (any color) in 3+ total contests, or took gold in 3+ consecutive contest ids; compute both sets and report the matching users

import pandas as pd

def find_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Condition 2: any medal in 3 or more contests
    medals = pd.concat([
        contests[['contest_id', 'gold_medal']].rename(columns={'gold_medal': 'user_id'}),
        contests[['contest_id', 'silver_medal']].rename(columns={'silver_medal': 'user_id'}),
        contests[['contest_id', 'bronze_medal']].rename(columns={'bronze_medal': 'user_id'}),
    ])
    total = medals.groupby('user_id').size()
    cond_medals = set(total[total >= 3].index)

    # Condition 1: gold in 3+ consecutive contests
    cond_gold = set()
    for uid, group in contests[['contest_id', 'gold_medal']].groupby('gold_medal'):
        ids = sorted(group['contest_id'])
        run = 1
        for i in range(1, len(ids)):
            run = run + 1 if ids[i] == ids[i - 1] + 1 else 1
            if run >= 3:
                cond_gold.add(uid)
                break

    candidates = cond_gold | cond_medals
    return users[users['user_id'].isin(candidates)][['name', 'mail']]
