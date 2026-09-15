# Author: Kaustav Ghosh
# Problem: Number of Unique Subjects Taught by Each Teacher
# Approach: A teacher can teach the same subject in several departments, so group the rows by teacher and count the distinct subject ids

import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    counts = teacher.groupby("teacher_id", as_index=False)["subject_id"].nunique()
    return counts.rename(columns={"subject_id": "cnt"})
