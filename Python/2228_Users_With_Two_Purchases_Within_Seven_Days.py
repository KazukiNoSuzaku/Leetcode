# Author: Kaustav Ghosh
# Problem: Users With Two Purchases Within Seven Days
# Approach: For each user, sort their purchase dates and look at consecutive gaps; if any gap is at most 7 days then that user has two purchases within a week (the closest pair is always consecutive after sorting). Return those user ids sorted

import pandas as pd


def users_with_two_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    df = purchases.copy()
    df["purchase_date"] = pd.to_datetime(df["purchase_date"])
    df = df.sort_values(["user_id", "purchase_date"])
    df["prev_date"] = df.groupby("user_id")["purchase_date"].shift(1)
    df["gap"] = (df["purchase_date"] - df["prev_date"]).dt.days
    eligible = df.loc[df["gap"] <= 7, "user_id"].unique()
    result = pd.DataFrame({"user_id": sorted(eligible)})
    return result
