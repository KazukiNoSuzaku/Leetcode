# Author: Kaustav Ghosh
# Problem: Find the Missing IDs (Premium)
# Approach: Build the full id range from 1 to the max present id, subtract the ids that exist, and return the gaps sorted

import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    max_id = customers['customer_id'].max()
    present = set(customers['customer_id'])
    missing = [i for i in range(1, max_id + 1) if i not in present]
    return pd.DataFrame({'ids': missing})
