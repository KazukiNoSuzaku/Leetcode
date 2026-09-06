# Author: Kaustav Ghosh
# Problem: Dynamic Pivoting of a Table
# Approach: Reshape the long Products table into a wide one: one row per product_id, one column per store (ordered alphabetically), holding the price or NULL where the product is not sold. pandas pivot handles this; sort the store columns and reset the index

import pandas as pd


def pivot_products(products: pd.DataFrame) -> pd.DataFrame:
    wide = products.pivot(index="product_id", columns="store", values="price")
    # store columns sorted lexicographically
    wide = wide.reindex(sorted(wide.columns), axis=1)
    wide = wide.reset_index()
    wide.columns.name = None
    return wide
