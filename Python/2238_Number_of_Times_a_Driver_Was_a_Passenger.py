# Author: Kaustav Ghosh
# Problem: Number of Times a Driver Was a Passenger
# Approach: Take the distinct driver ids, then for each count how many rides list that id as a passenger (zero if none). A left merge of the drivers against a passenger-count table, filling missing counts with zero, produces the result

import pandas as pd


def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    drivers = rides[["driver_id"]].drop_duplicates()
    passenger_counts = (
        rides.groupby("passenger_id").size().reset_index(name="cnt")
    )
    merged = drivers.merge(
        passenger_counts, how="left", left_on="driver_id", right_on="passenger_id"
    )
    merged["cnt"] = merged["cnt"].fillna(0).astype(int)
    return merged[["driver_id", "cnt"]]
