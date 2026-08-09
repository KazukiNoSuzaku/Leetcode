# Author: Kaustav Ghosh
# Problem: First and Last Call On the Same Day
# Approach: Expand every call into two rows so each participant is a "user" paired with the "other" party. Per user and calendar day, take the earliest and latest call by time; the user qualifies when both involved the same other person. Return distinct qualifying users

import pandas as pd

def first_and_last(calls: pd.DataFrame) -> pd.DataFrame:
    a = calls.rename(columns={'caller_id': 'user', 'recipient_id': 'other'})
    b = calls.rename(columns={'recipient_id': 'user', 'caller_id': 'other'})
    df = pd.concat([a[['user', 'other', 'call_time']],
                    b[['user', 'other', 'call_time']]], ignore_index=True)

    df['call_time'] = pd.to_datetime(df['call_time'])
    df['day'] = df['call_time'].dt.date
    df = df.sort_values('call_time')

    grp = df.groupby(['user', 'day'])
    first = grp.first().reset_index()
    last = grp.last().reset_index()

    merged = first.merge(last, on=['user', 'day'], suffixes=('_f', '_l'))
    ok = merged[merged['other_f'] == merged['other_l']]
    return ok[['user']].drop_duplicates().rename(columns={'user': 'user_id'})
