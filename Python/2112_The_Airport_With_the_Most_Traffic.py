# Author: Kaustav Ghosh
# Problem: The Airport With the Most Traffic
# Approach: Total traffic of an airport is its departing plus arriving flight counts. Sum both directions per airport and return the airport(s) achieving the maximum

import pandas as pd

def most_frequent_flights(flights: pd.DataFrame) -> pd.DataFrame:
    departures = flights.groupby('departure_airport')['flights_count'].sum()
    arrivals = flights.groupby('arrival_airport')['flights_count'].sum()
    total = departures.add(arrivals, fill_value=0)
    top = total[total == total.max()].index
    return pd.DataFrame({'airport_id': top})
