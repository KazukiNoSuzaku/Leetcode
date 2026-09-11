# Author: Kaustav Ghosh
# Problem: The First Day of the Maximum Recorded Degree in Each City
# Approach: For each city, find the day with the highest recorded degree, breaking ties by the earliest day. Sort by degree descending then day ascending, then keep the first row per city. Return ordered by city_id

import pandas as pd


def first_day_max_degree(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.sort_values(["degree", "day"], ascending=[False, True])
    result = df.groupby("city_id", as_index=False).first()
    result = result.sort_values("city_id")
    return result[["city_id", "day", "degree"]].reset_index(drop=True)
