# Author: Kaustav Ghosh
# Problem: The Category of Each Member in the Store
# Approach: For each member compute the conversion rate = 100 * visits-with-a-purchase / total-visits. Members with no visits are Bronze; otherwise Diamond (>=80), Gold (>=50), or Silver

import pandas as pd

def count_customer_category(members: pd.DataFrame, visits: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    v = visits.copy()
    v['bought'] = v['visit_id'].isin(set(purchases['visit_id']))
    agg = v.groupby('member_id').agg(total=('visit_id', 'count'),
                                     bought=('bought', 'sum')).reset_index()

    res = members.merge(agg, on='member_id', how='left')
    res['total'] = res['total'].fillna(0)
    res['bought'] = res['bought'].fillna(0)

    def category(row):
        if row['total'] == 0:
            return 'Bronze'
        rate = 100 * row['bought'] / row['total']
        if rate >= 80:
            return 'Diamond'
        if rate >= 50:
            return 'Gold'
        return 'Silver'

    res['category'] = res.apply(category, axis=1)
    return res[['member_id', 'name', 'category']]
