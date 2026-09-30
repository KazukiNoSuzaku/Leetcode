# Author: Kaustav Ghosh
# Problem: Concatenate the Name and the Profession
# Approach: Take the first character of the profession, wrap it in parentheses and glue it straight onto the name with no space, then order the rows by person id descending

import pandas as pd


def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:
    result = person.sort_values("person_id", ascending=False).copy()
    result["name"] = result["name"] + "(" + result["profession"].str[0] + ")"
    return result[["person_id", "name"]]
