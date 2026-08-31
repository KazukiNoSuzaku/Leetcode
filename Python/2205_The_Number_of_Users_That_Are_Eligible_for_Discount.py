# Author: Kaustav Ghosh
# Problem: The Number of Users That Are Eligible for Discount
# Approach: Filter purchases to those whose timestamp falls inside the inclusive [startDate, endDate] window (dates treated as day beginnings) and whose amount meets the minimum. Count the distinct qualifying users, returned as a single column user_cnt

import pandas as pd


def count_eligible_users(purchases: pd.DataFrame, start_date: str, end_date: str, min_amount: int) -> pd.DataFrame:
    start = pd.Timestamp(start_date)
    end = pd.Timestamp(end_date)
    mask = (
        (purchases["time_stamp"] >= start)
        & (purchases["time_stamp"] <= end)
        & (purchases["amount"] >= min_amount)
    )
    user_cnt = purchases.loc[mask, "user_id"].nunique()
    return pd.DataFrame({"user_cnt": [user_cnt]})
