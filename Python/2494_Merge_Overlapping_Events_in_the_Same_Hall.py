# Author: Kaustav Ghosh
# Problem: Merge Overlapping Events in the Same Hall
# Approach: Halls are independent, so sort each hall's events by start day and sweep them. An event that begins on or before the running end day extends it; otherwise the run is finished and a new one starts. Events merely touching across a day boundary share no day and stay separate

import pandas as pd


def merge_events(hall_events: pd.DataFrame) -> pd.DataFrame:
    events = hall_events.copy()
    events["start_day"] = pd.to_datetime(events["start_day"])
    events["end_day"] = pd.to_datetime(events["end_day"])
    events = events.sort_values(["hall_id", "start_day", "end_day"])
    merged = []
    for hall, group in events.groupby("hall_id", sort=False):
        current_start = current_end = None
        for start, end in zip(group["start_day"], group["end_day"]):
            if current_start is None:
                current_start, current_end = start, end
            elif start <= current_end:
                current_end = max(current_end, end)
            else:
                merged.append((hall, current_start, current_end))
                current_start, current_end = start, end
        if current_start is not None:
            merged.append((hall, current_start, current_end))
    return pd.DataFrame(merged, columns=["hall_id", "start_day", "end_day"])
