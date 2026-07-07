# Author: Kaustav Ghosh
# Problem: Hopper Company Queries II (Premium)
# Approach: Per 2020 month, active drivers = those joined by month-end; working_percentage = distinct drivers who accepted a ride that month / active drivers * 100 (0 when no active drivers)

import pandas as pd

def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    joined = pd.to_datetime(drivers['join_date'])
    result = pd.DataFrame({'month': range(1, 13)})

    def active_by(month):
        cutoff = pd.Timestamp(year=2020, month=month, day=1) + pd.offsets.MonthEnd(0)
        return int((joined <= cutoff).sum())

    result['active'] = result['month'].apply(active_by)

    merged = accepted_rides.merge(rides, on='ride_id')
    requested = pd.to_datetime(merged['requested_at'])
    in_2020 = merged[requested.dt.year == 2020].copy()
    in_2020['month'] = pd.to_datetime(in_2020['requested_at']).dt.month
    working = in_2020.groupby('month')['driver_id'].nunique()
    result['drivers'] = result['month'].map(working).fillna(0)

    result['working_percentage'] = result.apply(
        lambda r: round(r['drivers'] * 100.0 / r['active'], 2) if r['active'] > 0 else 0.0,
        axis=1,
    )
    return result[['month', 'working_percentage']]
