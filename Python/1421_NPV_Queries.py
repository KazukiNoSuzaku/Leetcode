# Author: Kaustav Ghosh
# Problem: NPV Queries (Premium SQL)
# Approach: LEFT JOIN Queries with NPV table, COALESCE null to 0
#
# SQL Solution:
# SELECT q.id, q.year, COALESCE(n.npv, 0) AS npv
# FROM Queries q
# LEFT JOIN NPV n ON q.id = n.id AND q.year = n.year

class Solution(object):
    pass
