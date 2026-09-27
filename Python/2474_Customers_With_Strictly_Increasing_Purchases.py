# Author: Kaustav Ghosh
# Problem: Customers With Strictly Increasing Purchases
# Approach: Total each customer's spending per calendar year, then look at the years from their first order to their last. A year with no orders counts as 0, so any gap in that span breaks the increase and rules the customer out; otherwise keep them when every year beats the one before

import pandas as pd


def increasing_purchases(orders: pd.DataFrame) -> pd.DataFrame:
    yearly = orders.assign(year=pd.to_datetime(orders["order_date"]).dt.year) \
                   .groupby(["customer_id", "year"], as_index=False)["price"].sum()
    kept = []
    for customer, group in yearly.groupby("customer_id"):
        ordered = group.sort_values("year")
        years = ordered["year"].tolist()
        prices = ordered["price"].tolist()
        if years[-1] - years[0] + 1 != len(years):
            continue
        if all(earlier < later for earlier, later in zip(prices, prices[1:])):
            kept.append(customer)
    return pd.DataFrame({"customer_id": kept})
