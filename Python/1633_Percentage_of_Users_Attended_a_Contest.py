# Author: Kaustav Ghosh
# Problem: Percentage of Users Attended a Contest
# Approach: Count distinct registrants per contest, divide by the total user count, round to 2 decimals, and order by percentage then contest id

import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total = len(users)
    result = (
        register.groupby('contest_id')['user_id']
                .nunique()
                .reset_index(name='attended')
    )
    result['percentage'] = (result['attended'] * 100.0 / total).round(2)
    result = result.sort_values(['percentage', 'contest_id'], ascending=[False, True])
    return result[['contest_id', 'percentage']]
