# Author: Kaustav Ghosh
# Problem: Customer Order Frequency (Premium)
# Approach: Join orders with product, compute monthly spend, filter customers with >= $100 in both June and July 2020

import pandas as pd

def get_customers(customers: pd.DataFrame, orders: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    orders = orders.merge(product, on='product_id')
    orders['spend'] = orders['quantity'] * orders['price']
    orders['month'] = pd.to_datetime(orders['order_date']).dt.to_period('M')

    june = orders[orders['month'] == '2020-06'].groupby('customer_id')['spend'].sum()
    july = orders[orders['month'] == '2020-07'].groupby('customer_id')['spend'].sum()

    valid_ids = set(june[june >= 100].index) & set(july[july >= 100].index)
    return customers[customers['customer_id'].isin(valid_ids)][['customer_id', 'name']]
