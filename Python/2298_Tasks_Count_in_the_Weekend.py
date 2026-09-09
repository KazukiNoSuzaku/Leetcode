# Author: Kaustav Ghosh
# Problem: Tasks Count in the Weekend
# Approach: Classify each task's submit_date by weekday: Saturday and Sunday (weekday index 5 and 6) are weekend, the rest are working days. Return a single row with the two counts

import pandas as pd


def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    weekday = pd.to_datetime(tasks["submit_date"]).dt.weekday
    weekend_cnt = int((weekday >= 5).sum())
    working_cnt = int((weekday < 5).sum())
    return pd.DataFrame({"weekend_cnt": [weekend_cnt], "working_cnt": [working_cnt]})
