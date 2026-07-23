# Author: Kaustav Ghosh
# Problem: Find Customers With Positive Revenue this Year (Premium)
# Approach: Filter to 2021 rows with revenue above zero and report those customer ids

import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    mask = (customers['year'] == 2021) & (customers['revenue'] > 0)
    return customers[mask][['customer_id']]
