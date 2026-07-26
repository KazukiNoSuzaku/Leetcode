# Author: Kaustav Ghosh
# Problem: Suspicious Bank Accounts (Premium)
# Approach: Sum Creditor income per account per month, flag months exceeding max_income, then mark accounts that have two calendar-adjacent flagged months

import pandas as pd

def suspicious_accounts(accounts: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    credit = transactions[transactions['type'] == 'Creditor'].copy()
    credit['month'] = pd.to_datetime(credit['day']).dt.to_period('M')
    monthly = credit.groupby(['account_id', 'month'], as_index=False)['amount'].sum()

    monthly = monthly.merge(accounts, on='account_id')
    over = monthly[monthly['amount'] > monthly['max_income']].sort_values(['account_id', 'month'])

    suspicious = set()
    prev_acc = None
    prev_month = None
    for acc, month in zip(over['account_id'], over['month']):
        if acc == prev_acc and (month - prev_month).n == 1:
            suspicious.add(acc)
        prev_acc, prev_month = acc, month

    return pd.DataFrame({'account_id': sorted(suspicious)})
