# Author: Kaustav Ghosh
# Problem: The Most Frequently Ordered Products for Each Customer (Premium)
# Approach: Count orders per (customer, product), keep the rows whose count ties the per-customer maximum, then attach product names

import pandas as pd

def most_frequent(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    counts = (
        orders.groupby(['customer_id', 'product_id'])
              .size()
              .reset_index(name='cnt')
    )
    counts['top'] = counts.groupby('customer_id')['cnt'].transform('max')
    best = counts[counts['cnt'] == counts['top']]
    return best.merge(products, on='product_id')[['customer_id', 'product_id', 'product_name']]
