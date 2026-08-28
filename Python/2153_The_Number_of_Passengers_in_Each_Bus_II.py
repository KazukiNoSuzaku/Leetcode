# Author: Kaustav Ghosh
# Problem: The Number of Passengers in Each Bus II
# Approach: Process buses in arrival order, carrying over the passengers still waiting. Each bus first admits everyone who has arrived by its time into the waiting pool, then boards up to its capacity; the rest wait for later buses

import pandas as pd

def count_passengers(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    ordered_buses = buses.sort_values('arrival_time').reset_index(drop=True)
    passenger_times = sorted(passengers['arrival_time'].tolist())

    results = []
    waiting = 0
    pi = 0
    total = len(passenger_times)
    for _, bus in ordered_buses.iterrows():
        while pi < total and passenger_times[pi] <= bus['arrival_time']:
            waiting += 1
            pi += 1
        board = min(waiting, int(bus['capacity']))
        waiting -= board
        results.append((bus['bus_id'], board))

    out = pd.DataFrame(results, columns=['bus_id', 'passengers_cnt'])
    return out.sort_values('bus_id')
