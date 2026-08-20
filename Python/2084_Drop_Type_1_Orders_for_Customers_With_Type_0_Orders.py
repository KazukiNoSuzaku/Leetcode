# Author: Kaustav Ghosh
# Problem: Drop Type 1 Orders for Customers With Type 0 Orders
# Approach: Identify customers who have any type-0 order. Keep every type-0 order, plus type-1 orders only for customers that have no type-0 order at all

import pandas as pd

def orders_analysis(orders: pd.DataFrame) -> pd.DataFrame:
    has_type0 = set(orders[orders['order_type'] == 0]['customer_id'])
    mask = (orders['order_type'] == 0) | (~orders['customer_id'].isin(has_type0))
    return orders[mask]
