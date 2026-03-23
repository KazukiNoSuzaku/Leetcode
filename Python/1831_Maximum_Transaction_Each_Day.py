# Author: Kaustav Ghosh
# Problem 1831: Maximum Transaction Each Day (Premium)
# SQL Problem - Solution in comments
#
# SELECT transaction_id
# FROM (
#     SELECT transaction_id,
#            RANK() OVER (PARTITION BY DATE(day) ORDER BY amount DESC) AS rk
#     FROM Transactions
# ) t
# WHERE rk = 1
# ORDER BY transaction_id;

class Solution(object):
    pass
