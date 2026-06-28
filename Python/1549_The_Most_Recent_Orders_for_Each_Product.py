# Author: Kaustav Ghosh
# Problem: The Most Recent Orders for Each Product (Premium)
# Approach: For each product keep rows whose order_date equals that product's max date (ties included), join with products for the name

import pandas as pd

def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = orders.copy()
    max_date = df.groupby('product_id')['order_date'].transform('max')
    recent = df[df['order_date'] == max_date]
    result = recent.merge(products, on='product_id')
    result = result[['product_name', 'product_id', 'order_id', 'order_date']]
    return result.sort_values(
        ['product_name', 'product_id', 'order_id']
    ).reset_index(drop=True)
