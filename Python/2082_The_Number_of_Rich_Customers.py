# Author: Kaustav Ghosh
# Problem: The Number of Rich Customers
# Approach: Count the distinct customers who have at least one bill with amount greater than 500

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_count = store[store['amount'] > 500]['customer_id'].nunique()
    return pd.DataFrame({'rich_count': [rich_count]})
