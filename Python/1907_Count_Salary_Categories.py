# Author: Kaustav Ghosh
# Problem: Count Salary Categories
# Approach: Count accounts in each income band (Low < 20000, Average in [20000, 50000], High > 50000) and always report all three categories, filling missing bands with zero

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    income = accounts['income']
    counts = {
        'Low Salary': int((income < 20000).sum()),
        'Average Salary': int(((income >= 20000) & (income <= 50000)).sum()),
        'High Salary': int((income > 50000).sum()),
    }
    return pd.DataFrame({
        'category': list(counts.keys()),
        'accounts_count': list(counts.values()),
    })
