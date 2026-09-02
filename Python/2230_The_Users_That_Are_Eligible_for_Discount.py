# Author: Kaustav Ghosh
# Problem: The Users That Are Eligible for Discount
# Approach: Keep purchases whose timestamp falls in the inclusive [startDate, endDate] window and whose amount meets the minimum, then return the distinct qualifying user ids ordered ascending

import pandas as pd


def eligible_users(purchases: pd.DataFrame, start_date: str, end_date: str, min_amount: int) -> pd.DataFrame:
    start = pd.Timestamp(start_date)
    end = pd.Timestamp(end_date)
    mask = (
        (purchases["time_stamp"] >= start)
        & (purchases["time_stamp"] <= end)
        & (purchases["amount"] >= min_amount)
    )
    ids = sorted(purchases.loc[mask, "user_id"].unique())
    return pd.DataFrame({"user_id": ids})
