# Author: Kaustav Ghosh
# Problem: Employees With Missing Information
# Approach: Outer-merge employees and salaries on employee_id; any row where name or salary is absent identifies an employee with missing information. Return those ids sorted

import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(salaries, on='employee_id', how='outer')
    missing = merged[merged['name'].isna() | merged['salary'].isna()]
    return missing[['employee_id']].sort_values('employee_id')
