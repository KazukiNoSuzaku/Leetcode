# Author: Kaustav Ghosh
# Problem: Calculate Salaries (Premium SQL)
# Approach: Find max salary per company, apply tax rate based on bracket
#
# SQL Solution:
# WITH company_max AS (
#     SELECT company_id, MAX(salary) AS max_salary
#     FROM Salaries
#     GROUP BY company_id
# )
# SELECT s.company_id, s.employee_id, s.employee_name,
#        ROUND(s.salary * CASE
#            WHEN cm.max_salary < 1000 THEN 1
#            WHEN cm.max_salary <= 10000 THEN 0.76
#            ELSE 0.51
#        END, 0) AS salary
# FROM Salaries s
# JOIN company_max cm ON s.company_id = cm.company_id

class Solution(object):
    pass
