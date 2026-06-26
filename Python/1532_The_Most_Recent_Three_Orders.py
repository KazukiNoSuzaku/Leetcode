# Author: Kaustav Ghosh
# Problem: The Most Recent Three Orders (Premium)
# Approach: Rank orders per customer by date descending, keep rank <= 3, join with customer names

import pandas as pd

def get_three_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.copy()
    orders['rn'] = orders.groupby('customer_id')['order_date'].rank(method='first', ascending=False)
    top3 = orders[orders['rn'] <= 3].merge(customers, on='customer_id')
    result = top3[['customer_name', 'customer_id', 'order_id', 'order_date']]
    return result.sort_values(
        ['customer_name', 'customer_id', 'order_date', 'order_id'],
        ascending=[True, True, False, True]
    )
