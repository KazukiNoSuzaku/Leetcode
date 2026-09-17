# Author: Kaustav Ghosh
# Problem: Sort the Olympic Table
# Approach: Order the table by gold, then silver, then bronze medals descending, falling back to the country name ascending for rows that tie on all three

import pandas as pd


def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    return olympic.sort_values(
        ["gold_medals", "silver_medals", "bronze_medals", "country"],
        ascending=[False, False, False, True]).reset_index(drop=True)
