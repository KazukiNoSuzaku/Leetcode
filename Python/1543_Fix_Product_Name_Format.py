# Author: Kaustav Ghosh
# Problem: Fix Product Name Format (Premium)
# Approach: Trim and lowercase product names, format sale_date as YYYY-MM, then count sales per product per month

import pandas as pd

def fix_product_name(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.copy()
    df['product_name'] = df['product_name'].str.strip().str.lower()
    df['sale_date'] = pd.to_datetime(df['sale_date']).dt.strftime('%Y-%m')
    result = (
        df.groupby(['product_name', 'sale_date'])
          .size()
          .reset_index(name='total')
    )
    return result.sort_values(['product_name', 'sale_date']).reset_index(drop=True)
