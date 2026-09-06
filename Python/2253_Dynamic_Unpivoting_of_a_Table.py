# Author: Kaustav Ghosh
# Problem: Dynamic Unpivoting of a Table
# Approach: Reverse of pivoting: melt the wide Products table (product_id plus one column per store) back into long rows of (product_id, store, price), dropping entries with no price (NULL). Order by product_id then store

import pandas as pd


def unpivot_products(products: pd.DataFrame) -> pd.DataFrame:
    long = products.melt(
        id_vars="product_id", var_name="store", value_name="price"
    )
    long = long.dropna(subset=["price"])
    long = long.sort_values(["product_id", "store"]).reset_index(drop=True)
    return long[["product_id", "store", "price"]]
