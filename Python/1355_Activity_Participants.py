# Author: Kaustav Ghosh
# Problem: Activity Participants (Premium SQL)
# Approach: Count activities that are neither the most nor least popular
#
# SQL Solution:
# SELECT activity
# FROM Friends
# GROUP BY activity
# HAVING COUNT(*) <> (SELECT MAX(cnt) FROM (SELECT COUNT(*) AS cnt FROM Friends GROUP BY activity) t)
#    AND COUNT(*) <> (SELECT MIN(cnt) FROM (SELECT COUNT(*) AS cnt FROM Friends GROUP BY activity) t)

class Solution(object):
    pass
