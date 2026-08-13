# Author: Kaustav Ghosh
# Problem: Number of Accounts That Did Not Stream
# Approach: An account counts if its subscription period overlaps the year 2021 but it has no stream dated in 2021. Filter subscriptions overlapping 2021, exclude accounts that streamed that year, and return the remaining ids

import pandas as pd

def accounts_not_streamed(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:
    subs = subscriptions.copy()
    subs['start_date'] = pd.to_datetime(subs['start_date'])
    subs['end_date'] = pd.to_datetime(subs['end_date'])
    low = pd.Timestamp('2021-01-01')
    high = pd.Timestamp('2021-12-31')
    active_2021 = subs[(subs['start_date'] <= high) & (subs['end_date'] >= low)]

    st = streams.copy()
    st['stream_date'] = pd.to_datetime(st['stream_date'])
    streamed_2021 = st[st['stream_date'].dt.year == 2021]['account_id']

    result = active_2021[~active_2021['account_id'].isin(streamed_2021)][['account_id']]
    return result.drop_duplicates()
