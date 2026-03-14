# Premium SQL problem - Running total of scores grouped by gender, ordered by day.

# Author: Kaustav Ghosh

# SQL solution:
# SELECT gender, day,
#   SUM(score_points) OVER (PARTITION BY gender ORDER BY day) AS total
# FROM Scores
# ORDER BY gender, day;

class Solution(object):
    pass
