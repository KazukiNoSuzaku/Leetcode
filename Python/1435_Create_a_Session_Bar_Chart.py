# Author: Kaustav Ghosh
# Problem: Create a Session Bar Chart (Premium SQL)
# Approach: CASE WHEN to bucket session durations into ranges
#
# SQL Solution:
# SELECT '[0-5>' AS bin, COUNT(*) AS total FROM Sessions WHERE duration >= 0 AND duration < 300
# UNION ALL
# SELECT '[5-10>' AS bin, COUNT(*) AS total FROM Sessions WHERE duration >= 300 AND duration < 600
# UNION ALL
# SELECT '[10-15>' AS bin, COUNT(*) AS total FROM Sessions WHERE duration >= 600 AND duration < 900
# UNION ALL
# SELECT '15 or more' AS bin, COUNT(*) AS total FROM Sessions WHERE duration >= 900

class Solution(object):
    pass
