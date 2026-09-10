# Author: Kaustav Ghosh
# Problem: Arrange Table by Gender
# Approach: The output cycles female, other, male, repeating. Within each gender order rows by user_id and give them a position (1st female, 1st other, 1st male, 2nd female, ...). Sort by that within-gender rank first, then by the fixed gender priority, to interleave the three groups

import pandas as pd


def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    priority = {"female": 0, "other": 1, "male": 2}
    df = genders.sort_values(["gender", "user_id"]).copy()
    df["rn"] = df.groupby("gender").cumcount()
    df["gp"] = df["gender"].map(priority)
    df = df.sort_values(["rn", "gp"])
    return df[["user_id", "gender"]].reset_index(drop=True)
