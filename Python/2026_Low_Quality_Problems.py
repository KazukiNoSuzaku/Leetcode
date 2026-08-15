# Author: Kaustav Ghosh
# Problem: Low-Quality Problems
# Approach: Keep problems whose like ratio likes/(likes+dislikes) is strictly below 60%, returned sorted by problem_id

import pandas as pd

def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    ratio = problems['likes'] / (problems['likes'] + problems['dislikes'])
    result = problems[ratio < 0.6]
    return result[['problem_id']].sort_values('problem_id')
