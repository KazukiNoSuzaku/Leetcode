# Author: Kaustav Ghosh
# Problem: Find Total Time Spent by Each Employee
# Approach: Each row contributes out_time - in_time; sum those per (day, employee)

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.copy()
    df['total_time'] = df['out_time'] - df['in_time']
    result = df.groupby(['event_day', 'emp_id'], as_index=False)['total_time'].sum()
    return result.rename(columns={'event_day': 'day'})
