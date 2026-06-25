# Author: Kaustav Ghosh
# Problem: Patients With a Condition
# Approach: Filter rows where conditions contains a word starting with 'DIAB1' using regex word-boundary pattern

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'(?:^| )DIAB1', regex=True)]
