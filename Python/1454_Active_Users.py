# Author: Kaustav Ghosh
# Problem: Active Users (Premium SQL)
# Approach: Self-join or window function to find 5 consecutive login days
#
# SQL Solution:
# WITH ranked AS (
#     SELECT DISTINCT id, login_date,
#            DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER (PARTITION BY id ORDER BY login_date) DAY) AS grp
#     FROM Logins
# )
# SELECT DISTINCT r.id, a.name
# FROM ranked r
# JOIN Accounts a ON r.id = a.id
# GROUP BY r.id, a.name, r.grp
# HAVING COUNT(*) >= 5
# ORDER BY r.id

class Solution(object):
    pass
