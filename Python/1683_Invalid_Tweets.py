# Author: Kaustav Ghosh
# Problem: Invalid Tweets
# Approach: Keep tweets whose content length exceeds 15 and report their ids

import pandas as pd

def invalid_tweets(Tweets: pd.DataFrame) -> pd.DataFrame:
    return Tweets[Tweets['content'].str.len() > 15][['tweet_id']]
