# Author: Kaustav Ghosh
# Problem: Count Apples and Oranges (Premium)
# Approach: Left-join each box to its chest (missing chests count as zero), then total the box fruit plus whatever the chest inside holds

import pandas as pd

def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:
    merged = boxes.merge(chests, on='chest_id', how='left', suffixes=('_box', '_chest'))
    merged = merged.fillna(0)
    apples = (merged['apple_count_box'] + merged['apple_count_chest']).sum()
    oranges = (merged['orange_count_box'] + merged['orange_count_chest']).sum()
    return pd.DataFrame({'apple_count': [int(apples)], 'orange_count': [int(oranges)]})
