# Author: Kaustav Ghosh
# Problem: Recyclable and Low Fat Products
# Approach: Keep the products flagged both low fat and recyclable, and report their ids

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products[mask][['product_id']]
