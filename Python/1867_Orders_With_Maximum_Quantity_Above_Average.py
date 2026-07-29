# Author: Kaustav Ghosh
# Problem: Orders With Maximum Quantity Above Average (Premium)
# Approach: Per order, compare its maximum single-item quantity against its average quantity; keep orders whose max strictly exceeds every order's average

import pandas as pd

def orders_above_avg(orders_details: pd.DataFrame) -> pd.DataFrame:
    stats = orders_details.groupby('order_id')['quantity'].agg(['max', 'mean'])
    highest_average = stats['mean'].max()
    imbalanced = stats[stats['max'] > highest_average]
    return imbalanced.reset_index()[['order_id']].sort_values('order_id')
