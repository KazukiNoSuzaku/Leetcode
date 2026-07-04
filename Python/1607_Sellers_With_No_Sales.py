# Author: Kaustav Ghosh
# Problem: Sellers With No Sales (Premium)
# Approach: Collect seller ids that appear in 2020 orders, then return sellers absent from that set, ordered by name

import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    sold_2020 = orders.loc[pd.to_datetime(orders['sale_date']).dt.year == 2020, 'seller_id']
    idle = seller[~seller['seller_id'].isin(sold_2020)]
    return idle.sort_values('seller_name')[['seller_name']]
