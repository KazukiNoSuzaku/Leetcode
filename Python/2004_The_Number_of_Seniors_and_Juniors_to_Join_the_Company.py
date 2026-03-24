# Author: Kaustav Ghosh
# Problem 2004: The Number of Seniors and Juniors to Join the Company (Premium)
#
# SQL Solution (Premium):
# WITH senior_cte AS (
#     SELECT employee_id, salary,
#            SUM(salary) OVER (ORDER BY salary, employee_id) AS running_total
#     FROM Candidates WHERE experience = 'Senior'
# ),
# junior_cte AS (
#     SELECT employee_id, salary,
#            SUM(salary) OVER (ORDER BY salary, employee_id) AS running_total
#     FROM Candidates WHERE experience = 'Junior'
# ),
# hired_seniors AS (
#     SELECT * FROM senior_cte WHERE running_total <= 70000
# )
# SELECT 'Senior' AS experience, COUNT(*) AS accepted_candidates FROM hired_seniors
# UNION ALL
# SELECT 'Junior', COUNT(*) FROM junior_cte
# WHERE running_total <= 70000 - COALESCE((SELECT MAX(running_total) FROM hired_seniors), 0);

class Solution(object):
    pass
