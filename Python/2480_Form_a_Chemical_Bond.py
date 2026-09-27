# Author: Kaustav Ghosh
# Problem: Form a Chemical Bond
# Approach: A bond needs one metal and one nonmetal, and noble elements bond with nothing, so split the table into those two groups and cross join them to list every possible pairing

import pandas as pd


def find_bonds(elements: pd.DataFrame) -> pd.DataFrame:
    metals = elements.loc[elements["type"] == "Metal", ["symbol"]].rename(
        columns={"symbol": "metal"})
    nonmetals = elements.loc[elements["type"] == "Nonmetal", ["symbol"]].rename(
        columns={"symbol": "nonmetal"})
    return metals.merge(nonmetals, how="cross")
