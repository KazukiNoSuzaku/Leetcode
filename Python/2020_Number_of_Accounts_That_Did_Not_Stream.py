# Author: Kaustav Ghosh
# Problem 2020: Number of Accounts That Did Not Stream (Premium)
#
# SQL Solution (Premium):
# SELECT COUNT(*) AS accounts_count
# FROM Subscriptions s
# WHERE s.start_date <= '2021-12-31' AND s.end_date >= '2021-01-01'
#   AND s.account_id NOT IN (
#       SELECT account_id FROM Streams
#       WHERE stream_date BETWEEN '2021-01-01' AND '2021-12-31'
#   );

class Solution(object):
    pass
