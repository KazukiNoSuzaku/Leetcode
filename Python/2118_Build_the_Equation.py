# Author: Kaustav Ghosh
# Problem: Build the Equation
# Approach: Sort terms by power descending and render each as sign + |factor| + power part (X^p, X, or nothing for the constant). Concatenate, drop a leading '+', and append "=0"

import pandas as pd

def build_the_equation(terms: pd.DataFrame) -> pd.DataFrame:
    ordered = terms.sort_values('power', ascending=False)
    pieces = []
    for _, row in ordered.iterrows():
        power = int(row['power'])
        factor = int(row['factor'])
        sign = '+' if factor > 0 else '-'
        magnitude = abs(factor)
        if power >= 2:
            x_part = 'X^' + str(power)
        elif power == 1:
            x_part = 'X'
        else:
            x_part = ''
        pieces.append(sign + str(magnitude) + x_part)

    equation = ''.join(pieces)
    if equation.startswith('+'):
        equation = equation[1:]
    equation += '=0'
    return pd.DataFrame({'equation': [equation]})
