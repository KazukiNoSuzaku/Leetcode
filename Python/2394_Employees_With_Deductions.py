# Author: Kaustav Ghosh
# Problem: Employees With Deductions
# Approach: Round every session up to whole minutes (negated floor division gives the ceiling), sum those minutes per employee, and map the totals onto the full employee list so people with no sessions count as 0. Anyone whose minutes fall short of needed_hours * 60 gets a deduction

import pandas as pd


def employees_with_deductions(employees: pd.DataFrame, logs: pd.DataFrame) -> pd.DataFrame:
    session = pd.to_datetime(logs["out_time"]) - pd.to_datetime(logs["in_time"])
    minutes = -(-session.dt.total_seconds() // 60)
    worked = minutes.groupby(logs["employee_id"]).sum()
    total = employees["employee_id"].map(worked).fillna(0)
    return employees.loc[total < employees["needed_hours"] * 60, ["employee_id"]]
