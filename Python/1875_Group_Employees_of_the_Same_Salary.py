# Author: Kaustav Ghosh
# Problem 1875: Group Employees of the Same Salary (Premium)
# SQL Problem - Solution in comments
#
# SELECT e.employee_id, e.name, e.salary,
#        DENSE_RANK() OVER (ORDER BY e.salary) AS team_id
# FROM Employees e
# WHERE e.salary IN (
#     SELECT salary FROM Employees GROUP BY salary HAVING COUNT(*) > 1
# )
# ORDER BY team_id, employee_id;

class Solution(object):
    pass
