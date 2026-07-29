# Author: Kaustav Ghosh
# Problem: Calculate Special Bonus
# Approach: Bonus equals salary only for employees with an odd id whose name does not start with 'M'; everyone else gets 0

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.copy()
    eligible = (df['employee_id'] % 2 == 1) & (~df['name'].str.startswith('M'))
    df['bonus'] = df['salary'].where(eligible, 0)
    return df[['employee_id', 'bonus']].sort_values('employee_id')
