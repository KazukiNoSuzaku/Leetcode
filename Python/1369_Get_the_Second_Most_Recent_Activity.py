# Author: Kaustav Ghosh
# Problem: Get the Second Most Recent Activity (Premium SQL)
# Approach: Window function to rank activities, pick second or only one if single activity
#
# SQL Solution:
# WITH ranked AS (
#     SELECT *, COUNT(*) OVER (PARTITION BY username) AS cnt,
#            ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) AS rn
#     FROM UserActivity
# )
# SELECT username, activity, startDate, endDate
# FROM ranked
# WHERE rn = 2 OR cnt = 1

class Solution(object):
    pass
