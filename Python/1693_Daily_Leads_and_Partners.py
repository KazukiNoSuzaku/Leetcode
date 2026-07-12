# Author: Kaustav Ghosh
# Problem: Daily Leads and Partners
# Approach: Group by (date_id, make_name) and count the distinct leads and distinct partners in each group

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id', 'make_name'], as_index=False).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique'),
    )
