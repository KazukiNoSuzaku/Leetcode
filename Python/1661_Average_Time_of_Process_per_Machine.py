# Author: Kaustav Ghosh
# Problem: Average Time of Process per Machine
# Approach: Join each process's start and end rows, take end-start per process, then average per machine rounded to 3 decimals

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    starts = activity[activity['activity_type'] == 'start']
    ends = activity[activity['activity_type'] == 'end']
    merged = starts.merge(ends, on=['machine_id', 'process_id'])
    merged['elapsed'] = merged['timestamp_y'] - merged['timestamp_x']
    result = merged.groupby('machine_id', as_index=False)['elapsed'].mean()
    result['processing_time'] = result['elapsed'].round(3)
    return result[['machine_id', 'processing_time']]
