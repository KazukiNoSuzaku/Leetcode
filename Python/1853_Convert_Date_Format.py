# Author: Kaustav Ghosh
# Problem: Convert Date Format (Premium)
# Approach: Parse the date and reformat it as "Weekday, Month Day, Year" with strftime (no leading zero on the day)

import pandas as pd

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
    parsed = pd.to_datetime(days['day'])
    days['day'] = parsed.dt.strftime('%A, %B %-d, %Y')
    return days
