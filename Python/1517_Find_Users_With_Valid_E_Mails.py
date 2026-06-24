# Author: Kaustav Ghosh
# Problem: Find Users With Valid E-Mails
# Approach: Regex match — prefix starts with letter, contains only letters/digits/.-_, domain is @leetcode.com

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.\-]*@leetcode\.com$'
    return users[users['mail'].str.match(pattern)]
