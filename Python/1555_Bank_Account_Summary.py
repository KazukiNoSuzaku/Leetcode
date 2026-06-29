# Author: Kaustav Ghosh
# Problem: Bank Account Summary (Premium)
# Approach: Sum each user's transaction amounts onto their starting credit, then flag accounts whose final balance is negative

import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    deltas = (
        transactions.groupby('user_id')['amount']
        .sum()
        .reset_index(name='delta')
    )
    df = users.merge(deltas, on='user_id', how='left')
    df['delta'] = df['delta'].fillna(0)
    df['credit'] = df['credit'] + df['delta']
    df['credit_limit_breached'] = df['credit'].apply(lambda c: 'Yes' if c < 0 else 'No')
    return df[['user_id', 'user_name', 'credit', 'credit_limit_breached']]
