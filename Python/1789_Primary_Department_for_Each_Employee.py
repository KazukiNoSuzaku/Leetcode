# Author: Kaustav Ghosh
# Problem: Primary Department for Each Employee
# Approach: Keep every row flagged primary ('Y'), plus employees who belong to just one department (that lone row is primary by default)

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    flagged = employee[employee['primary_flag'] == 'Y']

    counts = employee['employee_id'].value_counts()
    single = employee[employee['employee_id'].isin(counts[counts == 1].index)]

    result = pd.concat([flagged, single])
    return result[['employee_id', 'department_id']]
