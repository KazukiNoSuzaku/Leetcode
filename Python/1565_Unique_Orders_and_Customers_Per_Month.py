# Author: Kaustav Ghosh
# Problem: Unique Orders and Customers Per Month (Premium)
# Approach: Keep orders with invoice > 20, bucket by YYYY-MM, then count distinct orders and distinct customers per month

import pandas as pd

def count_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders[orders['invoice'] > 20].copy()
    df['month'] = pd.to_datetime(df['order_date']).dt.strftime('%Y-%m')
    return (
        df.groupby('month')
          .agg(order_count=('order_id', 'nunique'),
               customer_count=('customer_id', 'nunique'))
          .reset_index()
    )
