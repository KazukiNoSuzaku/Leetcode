# Author: Kaustav Ghosh
# Problem 2072: The Winner University (Premium)
# SQL Problem:
# SELECT
#   CASE
#     WHEN (SELECT COUNT(*) FROM NewYork WHERE score >= 90)
#       > (SELECT COUNT(*) FROM California WHERE score >= 90)
#     THEN 'New York University'
#     WHEN (SELECT COUNT(*) FROM NewYork WHERE score >= 90)
#       < (SELECT COUNT(*) FROM California WHERE score >= 90)
#     THEN 'California University'
#     ELSE 'No Winner'
#   END AS winner;

class Solution(object):
    pass
