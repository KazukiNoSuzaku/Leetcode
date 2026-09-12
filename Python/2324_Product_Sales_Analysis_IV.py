# Author: Kaustav Ghosh
# Problem: Product Sales Analysis IV
# Approach: Join sales to product prices and sum quantity*price per (user_id, product_id). For each user find the maximum total spend, then keep every product matching that maximum (ties included). Return user_id and product_id

import pandas as pd


def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = sales.merge(product, on="product_id")
    merged["spend"] = merged["quantity"] * merged["price"]
    per = merged.groupby(["user_id", "product_id"], as_index=False)["spend"].sum()
    per["mx"] = per.groupby("user_id")["spend"].transform("max")
    result = per[per["spend"] == per["mx"]]
    return result[["user_id", "product_id"]].reset_index(drop=True)
