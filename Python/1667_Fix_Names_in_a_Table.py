# Author: Kaustav Ghosh
# Problem: Fix Names in a Table
# Approach: Capitalize each name (first letter upper, rest lower) and order by user id

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')
