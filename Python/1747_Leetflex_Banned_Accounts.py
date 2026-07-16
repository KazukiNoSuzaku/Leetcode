# Author: Kaustav Ghosh
# Problem: Leetflex Banned Accounts (Premium)
# Approach: Self-join each account's sessions; an account is banned when one session's login falls inside another session that used a different IP

import pandas as pd

def leetflex_banned_accounts(log_info: pd.DataFrame) -> pd.DataFrame:
    pairs = log_info.merge(log_info, on='account_id', suffixes=('_a', '_b'))
    overlapping = pairs[
        (pairs['ip_address_a'] != pairs['ip_address_b'])
        & (pairs['login_a'] >= pairs['login_b'])
        & (pairs['login_a'] <= pairs['logout_b'])
    ]
    return overlapping[['account_id']].drop_duplicates()
