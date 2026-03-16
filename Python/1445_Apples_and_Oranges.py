# Author: Kaustav Ghosh
# Problem: Apples & Oranges (Premium SQL)
# Approach: Pivot sales by fruit, compute difference per date
#
# SQL Solution:
# SELECT sale_date,
#        SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE -sold_num END) AS diff
# FROM Sales
# GROUP BY sale_date
# ORDER BY sale_date

class Solution(object):
    pass
