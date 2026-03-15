# Premium SQL problem - Compute 7-day moving average of customer amounts.

# Author: Kaustav Ghosh

# SQL solution:
# SELECT visited_on,
#   SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
#   ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
# FROM (SELECT visited_on, SUM(amount) AS amount FROM Customer GROUP BY visited_on) t
# WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer) + 6;

class Solution(object):
    pass
