# Author: Kaustav Ghosh
# Problem 1873: Calculate Special Bonus
# SQL Problem - Solution in comments
#
# SELECT employee_id,
#        CASE
#            WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
#            ELSE 0
#        END AS bonus
# FROM Employees
# ORDER BY employee_id;

class Solution(object):
    pass
