# Author: Kaustav Ghosh
# Problem: The Number of Employees Which Report to Each Employee
# Approach: Group the employees who have a manager by that manager, count them and average their ages, then join back to get the manager's name

import numpy as np
import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    reports = employees[employees['reports_to'].notna()]
    agg = reports.groupby('reports_to', as_index=False).agg(
        reports_count=('employee_id', 'count'),
        average_age=('age', 'mean'),
    )
    # SQL ROUND is half-up, unlike pandas' banker's rounding
    agg['average_age'] = np.floor(agg['average_age'] + 0.5).astype(int)

    df = employees.merge(agg, left_on='employee_id', right_on='reports_to')
    return df[['employee_id', 'name', 'reports_count', 'average_age']].sort_values('employee_id')
