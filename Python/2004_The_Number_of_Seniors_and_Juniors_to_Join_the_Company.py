# Author: Kaustav Ghosh
# Problem: The Number of Seniors and Juniors to Join the Company
# Approach: With a 70000 budget, hire as many seniors as possible in ascending salary order (prefix sums), then spend the leftover budget on juniors the same way. Report both counts

import pandas as pd

def count_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    budget = 70000

    seniors = candidates[candidates['experience'] == 'Senior'].sort_values('salary')
    senior_cumsum = seniors['salary'].cumsum()
    senior_hired = int((senior_cumsum <= budget).sum())
    senior_spent = int(senior_cumsum[senior_cumsum <= budget].max()) if senior_hired else 0

    remaining = budget - senior_spent
    juniors = candidates[candidates['experience'] == 'Junior'].sort_values('salary')
    junior_cumsum = juniors['salary'].cumsum()
    junior_hired = int((junior_cumsum <= remaining).sum())

    return pd.DataFrame({
        'experience': ['Senior', 'Junior'],
        'accepted_candidates': [senior_hired, junior_hired],
    })
