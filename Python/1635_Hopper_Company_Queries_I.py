# Author: Kaustav Ghosh
# Problem: Hopper Company Queries I (Premium)
# Approach: For each month 1..12 of 2020, count drivers who had joined by that month's end and the accepted rides requested that month

import pandas as pd

def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    joined = pd.to_datetime(drivers['join_date'])

    result = pd.DataFrame({'month': range(1, 13)})

    def active_by(month):
        cutoff = pd.Timestamp(year=2020, month=month, day=1) + pd.offsets.MonthEnd(0)
        return int((joined <= cutoff).sum())

    result['active_drivers'] = result['month'].apply(active_by)

    merged = accepted_rides.merge(rides, on='ride_id')
    requested = pd.to_datetime(merged['requested_at'])
    in_2020 = merged[requested.dt.year == 2020]
    per_month = in_2020.groupby(pd.to_datetime(in_2020['requested_at']).dt.month).size()

    result['accepted_rides'] = result['month'].map(per_month).fillna(0).astype(int)
    return result
