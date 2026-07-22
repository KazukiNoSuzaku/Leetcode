# Author: Kaustav Ghosh
# Problem: Ad-Free Sessions (Premium)
# Approach: Gather the session_ids that showed an ad, then report the sessions absent from that set

import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    with_ads = playback.merge(ads, on='customer_id')
    ad_shown = with_ads[
        (with_ads['timestamp'] >= with_ads['start_time'])
        & (with_ads['timestamp'] <= with_ads['end_time'])
    ]
    blocked = set(ad_shown['session_id'])
    clean = playback[~playback['session_id'].isin(blocked)]
    return clean[['session_id']]
