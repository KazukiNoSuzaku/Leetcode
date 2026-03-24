# Author: Kaustav Ghosh
# Problem 2010: The Number of Seniors and Juniors to Join the Company II (Premium)
#
# SQL Solution (Premium):
# Similar to 2004 but returns actual employee_ids instead of counts.
# WITH senior_cte AS (
#     SELECT employee_id,
#            SUM(salary) OVER (ORDER BY salary, employee_id) AS running_total
#     FROM Candidates WHERE experience = 'Senior'
# ),
# hired_seniors AS (
#     SELECT employee_id, running_total FROM senior_cte WHERE running_total <= 70000
# ),
# remaining AS (
#     SELECT 70000 - COALESCE(MAX(running_total), 0) AS budget FROM hired_seniors
# ),
# junior_cte AS (
#     SELECT employee_id,
#            SUM(salary) OVER (ORDER BY salary, employee_id) AS running_total
#     FROM Candidates WHERE experience = 'Junior'
# )
# SELECT employee_id FROM hired_seniors
# UNION ALL
# SELECT employee_id FROM junior_cte, remaining WHERE running_total <= budget;

class Solution(object):
    pass
