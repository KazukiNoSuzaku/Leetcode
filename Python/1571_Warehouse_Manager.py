# Author: Kaustav Ghosh
# Problem: Warehouse Manager (Premium)
# Approach: Compute each product's volume (Width*Length*Height), join onto warehouse stock, then sum units*volume per warehouse

import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    products = products.copy()
    products['volume'] = products['Width'] * products['Length'] * products['Height']
    df = warehouse.merge(products[['product_id', 'volume']], on='product_id')
    df['volume'] = df['units'] * df['volume']
    return (
        df.groupby('name', as_index=False)['volume'].sum()
          .rename(columns={'name': 'warehouse_name'})
    )
