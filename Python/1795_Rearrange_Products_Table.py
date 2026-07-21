# Author: Kaustav Ghosh
# Problem: Rearrange Products Table
# Approach: Unpivot the three store columns into (product_id, store, price) rows and drop the entries with no price

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    melted = products.melt(
        id_vars='product_id',
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price',
    )
    return melted.dropna(subset=['price'])
