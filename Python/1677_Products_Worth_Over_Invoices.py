# Author: Kaustav Ghosh
# Problem: Product's Worth Over Invoices (Premium)
# Approach: Sum rest/paid/canceled/refunded per product over its invoices, attach the product name, and order by name

import pandas as pd

def sum_of_all(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:
    totals = invoice.groupby('product_id', as_index=False).agg(
        rest=('rest', 'sum'),
        paid=('paid', 'sum'),
        canceled=('canceled', 'sum'),
        refunded=('refunded', 'sum'),
    )
    df = totals.merge(product, on='product_id')
    df = df.sort_values('name')
    return df[['name', 'rest', 'paid', 'canceled', 'refunded']]
