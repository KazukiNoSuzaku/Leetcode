# Author: Kaustav Ghosh
# Problem: Countries You Can Safely Invest In (Premium)
# Approach: Join persons to country via phone prefix, compare per-country avg duration to global avg

import pandas as pd

def find_safe_investment_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    person = person.copy()
    person['country_code'] = person['phone_number'].str[:3]
    person = person.merge(country, on='country_code')[['id', 'name']]

    global_avg = calls['duration'].mean()

    caller = calls.merge(person, left_on='caller_id', right_on='id')[['duration', 'name']]
    callee = calls.merge(person, left_on='callee_id', right_on='id')[['duration', 'name']]

    all_calls = pd.concat([caller, callee])
    result = all_calls.groupby('name', as_index=False)['duration'].mean()
    return result[result['duration'] > global_avg][['name']].rename(columns={'name': 'country'})
