# Author: Kaustav Ghosh
# Problem: Group Employees of the Same Salary (Premium)
# Approach: Keep only salaries shared by more than one employee, then assign each surviving salary a team_id by its dense rank; order by team then employee

import pandas as pd

def group_sorted(employees: pd.DataFrame) -> pd.DataFrame:
    shared = employees.groupby('salary')['employee_id'].transform('count') > 1
    df = employees[shared].copy()
    df['team_id'] = df['salary'].rank(method='dense').astype(int)
    df = df.sort_values(['team_id', 'employee_id'])
    return df[['employee_id', 'name', 'salary', 'team_id']]
