# Author: Kaustav Ghosh
# Problem: Number of Calls Between Two Persons (Premium)
# Approach: Normalize each call to an unordered pair (min id, max id), then group to count calls and sum durations per pair

import pandas as pd

def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    df = calls.copy()
    df['person1'] = df[['from_id', 'to_id']].min(axis=1)
    df['person2'] = df[['from_id', 'to_id']].max(axis=1)
    return df.groupby(['person1', 'person2'], as_index=False).agg(
        call_count=('duration', 'count'),
        total_duration=('duration', 'sum'),
    )
