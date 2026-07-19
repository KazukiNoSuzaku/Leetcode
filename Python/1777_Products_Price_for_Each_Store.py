# Author: Kaustav Ghosh
# Problem: Products Price for Each Store (Premium)
# Approach: Pivot the long (product, store, price) table into one column per store, keeping missing store prices as null

import pandas as pd

def products_price(products: pd.DataFrame) -> pd.DataFrame:
    pivoted = products.pivot(index='product_id', columns='store', values='price')
    pivoted = pivoted.reset_index()
    pivoted.columns.name = None
    for store in ('store1', 'store2', 'store3'):
        if store not in pivoted.columns:
            pivoted[store] = None
    return pivoted[['product_id', 'store1', 'store2', 'store3']]
