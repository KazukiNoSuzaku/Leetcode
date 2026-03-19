# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-the-missing-ids/
# SQL Problem (Premium)
#
# WITH RECURSIVE seq AS (
#     SELECT 1 AS ids
#     UNION ALL
#     SELECT ids + 1 FROM seq WHERE ids < (SELECT MAX(customer_id) FROM Customers)
# )
# SELECT ids
# FROM seq
# WHERE ids NOT IN (SELECT customer_id FROM Customers);

class Solution(object):
    pass
