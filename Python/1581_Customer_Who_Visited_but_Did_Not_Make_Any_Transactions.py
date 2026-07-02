# Author: Kaustav Ghosh
# Problem: Customer Who Visited but Did Not Make Any Transactions
# Approach: Left-join visits to transactions; rows with no matching transaction are empty visits, count them per customer

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = visits.merge(transactions, on='visit_id', how='left')
    empty = merged[merged['transaction_id'].isna()]
    return (
        empty.groupby('customer_id')
             .size()
             .reset_index(name='count_no_trans')
    )
