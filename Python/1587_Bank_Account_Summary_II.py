# Author: Kaustav Ghosh
# Problem: Bank Account Summary II
# Approach: Sum transaction amounts per account for the balance, join names, and keep only accounts with balance above 10000

import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    balances = (
        transactions.groupby('account', as_index=False)['amount']
                    .sum()
                    .rename(columns={'amount': 'balance'})
    )
    df = users.merge(balances, on='account')
    return df.loc[df['balance'] > 10000, ['name', 'balance']]
