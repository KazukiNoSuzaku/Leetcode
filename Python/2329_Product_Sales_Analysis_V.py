# Author: Kaustav Ghosh
# Problem: Product Sales Analysis V
# Approach: Join sales to product prices, compute each user's total spending as the sum of quantity*price, then return user_id and spending ordered by spending descending and user_id ascending

import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = sales.merge(product, on="product_id")
    merged["amount"] = merged["quantity"] * merged["price"]
    spending = merged.groupby("user_id", as_index=False)["amount"].sum()
    spending = spending.rename(columns={"amount": "spending"})
    spending = spending.sort_values(["spending", "user_id"], ascending=[False, True])
    return spending[["user_id", "spending"]].reset_index(drop=True)
