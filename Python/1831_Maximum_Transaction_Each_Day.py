# Author: Kaustav Ghosh
# Problem: Maximum Transaction Each Day (Premium)
# Approach: For each calendar day keep the transactions whose amount equals that day's maximum, then report their ids ordered

import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.copy()
    df['day'] = pd.to_datetime(df['day']).dt.date
    df['day_max'] = df.groupby('day')['amount'].transform('max')
    result = df[df['amount'] == df['day_max']]
    return result[['transaction_id']].sort_values('transaction_id')
