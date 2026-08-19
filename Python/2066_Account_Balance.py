# Author: Kaustav Ghosh
# Problem: Account Balance
# Approach: Turn each transaction into a signed amount (deposits positive, withdrawals negative), then take a per-account running cumulative sum ordered by day to get the balance after each transaction

import pandas as pd

def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.sort_values(['account_id', 'day']).copy()
    df['signed'] = df['amount'].where(df['type'] == 'Deposit', -df['amount'])
    df['balance'] = df.groupby('account_id')['signed'].cumsum()
    return df[['account_id', 'day', 'balance']]
