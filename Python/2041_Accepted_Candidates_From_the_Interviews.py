# Author: Kaustav Ghosh
# Problem: Accepted Candidates From the Interviews
# Approach: Sum each interview's round scores, join to candidates, and keep those with at least two years of experience and a total interview score above 15

import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    totals = rounds.groupby('interview_id')['score'].sum().reset_index(name='total_score')
    merged = candidates.merge(totals, on='interview_id', how='left')
    accepted = merged[(merged['years_of_exp'] >= 2) & (merged['total_score'] > 15)]
    return accepted[['candidate_id']]
