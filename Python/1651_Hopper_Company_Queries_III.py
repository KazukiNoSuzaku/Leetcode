# Author: Kaustav Ghosh
# Problem: Hopper Company Queries III (Premium)
# Approach: Sum accepted-ride distance/duration per 2020 month, then for each starting month 1..10 average the totals over its three-month window

import pandas as pd

def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    merged = accepted_rides.merge(rides, on='ride_id')
    requested = pd.to_datetime(merged['requested_at'])
    merged = merged[requested.dt.year == 2020].copy()
    merged['month'] = pd.to_datetime(merged['requested_at']).dt.month

    dist = merged.groupby('month')['ride_distance'].sum()
    dur = merged.groupby('month')['ride_duration'].sum()
    monthly_dist = {m: float(dist.get(m, 0)) for m in range(1, 13)}
    monthly_dur = {m: float(dur.get(m, 0)) for m in range(1, 13)}

    rows = []
    for m in range(1, 11):
        avg_dist = (monthly_dist[m] + monthly_dist[m + 1] + monthly_dist[m + 2]) / 3.0
        avg_dur = (monthly_dur[m] + monthly_dur[m + 1] + monthly_dur[m + 2]) / 3.0
        rows.append({
            'month': m,
            'average_ride_distance': round(avg_dist, 2),
            'average_ride_duration': round(avg_dur, 2),
        })
    return pd.DataFrame(rows)
