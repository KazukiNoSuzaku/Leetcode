# Premium SQL problem - Compute click-through rate for each ad.
# CTR = clicks / (clicks + views) * 100, rounded to 2 decimals. 0 if no clicks or views.

# Author: Kaustav Ghosh

# SQL solution:
# SELECT ad_id,
#   ROUND(
#     IFNULL(SUM(action='Clicked') / NULLIF(SUM(action IN ('Clicked','Viewed')), 0) * 100, 0),
#     2
#   ) AS ctr
# FROM Ads
# GROUP BY ad_id
# ORDER BY ctr DESC, ad_id ASC;

class Solution(object):
    pass
