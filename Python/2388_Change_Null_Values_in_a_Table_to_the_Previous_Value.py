# Author: Kaustav Ghosh
# Problem: Change Null Values in a Table to the Previous Value
# Approach: The rows must stay in their input order, which is not sorted by id, so forward-fill the drink column exactly as the rows arrive; the first row is guaranteed to have a drink, so every null gets one

import pandas as pd


def change_null_values(coffee_shop: pd.DataFrame) -> pd.DataFrame:
    result = coffee_shop.copy()
    result["drink"] = result["drink"].ffill()
    return result
