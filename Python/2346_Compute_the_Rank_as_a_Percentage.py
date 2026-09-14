# Author: Kaustav Ghosh
# Problem: Compute the Rank as a Percentage
# Approach: Within each department rank marks descending (ties share the lower rank) and count the students, then compute (rank - 1) * 100 / (count - 1) rounded half-up to 2 decimals, which is 0 for a single-student department. The rounding is done in integer hundredths so exact ties like 3.125 round up the way SQL's ROUND does

import pandas as pd


def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
    by_dept = students.groupby("department_id")["mark"]
    rank = by_dept.rank(method="min", ascending=False).astype(int)
    others = by_dept.transform("size") - 1
    hundredths = ((rank - 1) * 20000 + others) // (2 * others).clip(lower=1)
    result = students[["student_id", "department_id"]].copy()
    result["percentage"] = hundredths / 100
    return result
