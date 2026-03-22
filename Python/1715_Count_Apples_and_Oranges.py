# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-apples-and-oranges/
# Premium Problem (SQL)
#
# SQL Solution:
# SELECT
#     SUM(b.apple_count + COALESCE(c.apple_count, 0)) AS apple_count,
#     SUM(b.orange_count + COALESCE(c.orange_count, 0)) AS orange_count
# FROM Boxes b
# LEFT JOIN Chests c ON b.chest_id = c.chest_id;

class Solution(object):
    pass
