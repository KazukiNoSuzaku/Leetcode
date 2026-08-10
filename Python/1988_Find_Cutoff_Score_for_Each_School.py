# Author: Kaustav Ghosh
# Problem: Find Cutoff Score for Each School
# Approach: Cross-join schools with the exam thresholds, keep rows where the applicant count fits the school's capacity, and take the minimum such score per school. Schools with no feasible threshold get -1

import pandas as pd

def cutoff_scores(schools: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    merged = schools.merge(exam, how='cross')
    feasible = merged[merged['student_count'] <= merged['capacity']]
    best = feasible.groupby('school_id')['score'].min().reset_index()

    result = schools[['school_id']].merge(best, on='school_id', how='left')
    result['score'] = result['score'].fillna(-1).astype(int)
    return result[['school_id', 'score']]
