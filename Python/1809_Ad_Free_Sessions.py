# Author: Kaustav Ghosh
# Premium problem - Ad-Free Sessions
# SQL: Find sessions with no ad played during them
# SELECT DISTINCT s.session_id
# FROM Playback s
# LEFT JOIN Ads a ON s.customer_id = a.customer_id
#     AND a.timestamp BETWEEN s.start_time AND s.end_time
# WHERE a.customer_id IS NULL;

class Solution(object):
    pass
