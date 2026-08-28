# Author: Kaustav Ghosh
# Problem: Order Two Columns Independently
# Approach: Sort the first column ascending and the second column descending independently, then pair them row by row

import pandas as pd

def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
    first = data['first_col'].sort_values(ascending=True).reset_index(drop=True)
    second = data['second_col'].sort_values(ascending=False).reset_index(drop=True)
    return pd.DataFrame({'first_col': first, 'second_col': second})
