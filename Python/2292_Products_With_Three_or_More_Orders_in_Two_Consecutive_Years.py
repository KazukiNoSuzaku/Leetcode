# Author: Kaustav Ghosh
# Problem: Products With Three or More Orders in Two Consecutive Years
# Approach: Count orders per (product_id, year) and keep only years where a product has at least three orders. A product qualifies if it has two such years that are consecutive: self-join the qualifying (product, year) rows on year differing by one. Return the distinct product ids

import pandas as pd


def products_with_three_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.copy()
    df["year"] = pd.to_datetime(df["purchase_date"]).dt.year
    counts = df.groupby(["product_id", "year"]).size().reset_index(name="cnt")
    qualified = counts[counts["cnt"] >= 3][["product_id", "year"]]
    merged = qualified.merge(qualified, on="product_id")
    consecutive = merged[merged["year_y"] - merged["year_x"] == 1]
    result = consecutive[["product_id"]].drop_duplicates().sort_values("product_id")
    return result.reset_index(drop=True)
