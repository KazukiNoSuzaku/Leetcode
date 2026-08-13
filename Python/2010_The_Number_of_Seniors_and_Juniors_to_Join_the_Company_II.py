# Author: Kaustav Ghosh
# Problem: The Number of Seniors and Juniors to Join the Company II
# Approach: Same greedy hiring as part I but return the actual ids. Take seniors in ascending salary while the running total stays within 70000, then spend the leftover budget on juniors the same way, and return every accepted employee_id

import pandas as pd

def open_positions(candidates: pd.DataFrame) -> pd.DataFrame:
    budget = 70000

    seniors = candidates[candidates['experience'] == 'Senior'].sort_values(['salary', 'employee_id'])
    seniors = seniors.assign(running=seniors['salary'].cumsum())
    hired_seniors = seniors[seniors['running'] <= budget]
    remaining = budget - int(hired_seniors['salary'].sum())

    juniors = candidates[candidates['experience'] == 'Junior'].sort_values(['salary', 'employee_id'])
    juniors = juniors.assign(running=juniors['salary'].cumsum())
    hired_juniors = juniors[juniors['running'] <= remaining]

    return pd.concat([hired_seniors[['employee_id']], hired_juniors[['employee_id']]])
