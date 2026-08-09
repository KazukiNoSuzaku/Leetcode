# Author: Kaustav Ghosh
# Problem: Employees Whose Manager Left the Company
# Approach: Keep employees earning under 30000 whose manager_id is set but no longer appears among current employee ids (the manager left). Return their ids sorted

import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    current_ids = set(employees['employee_id'])
    mask = (
        (employees['salary'] < 30000)
        & (employees['manager_id'].notna())
        & (~employees['manager_id'].isin(current_ids))
    )
    return employees[mask][['employee_id']].sort_values('employee_id')
