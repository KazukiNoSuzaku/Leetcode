# Author: Kaustav Ghosh
# Problem: The Number of Passengers in Each Bus I
# Approach: Process buses in arrival order; each takes every still-waiting passenger who arrived by its time. The count on a bus is the number of passengers arriving at or before it minus those already taken by earlier buses (a cumulative difference)

import pandas as pd
import numpy as np

def count_passengers(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    ordered = buses.sort_values('arrival_time').reset_index(drop=True)
    passenger_times = np.sort(passengers['arrival_time'].values)
    cumulative = np.searchsorted(passenger_times, ordered['arrival_time'].values, side='right')
    counts = np.diff(np.concatenate([[0], cumulative]))
    ordered['passengers_cnt'] = counts
    return ordered[['bus_id', 'passengers_cnt']].sort_values('bus_id')
