# Author: Kaustav Ghosh
# Problem: All Valid Triplets That Can Represent a Country (Premium)
# Approach: Cross-join the three schools, then keep only triplets whose three student ids are all distinct

import pandas as pd

def find_valid_triplets(SchoolA: pd.DataFrame, SchoolB: pd.DataFrame, SchoolC: pd.DataFrame) -> pd.DataFrame:
    a = SchoolA.rename(columns={'student_id': 'id_a', 'student_name': 'member_A'})
    b = SchoolB.rename(columns={'student_id': 'id_b', 'student_name': 'member_B'})
    c = SchoolC.rename(columns={'student_id': 'id_c', 'student_name': 'member_C'})
    df = a.merge(b, how='cross').merge(c, how='cross')
    df = df[(df['id_a'] != df['id_b']) & (df['id_b'] != df['id_c']) & (df['id_a'] != df['id_c'])]
    return df[['member_A', 'member_B', 'member_C']]
