-- Author: Kaustav Ghosh
-- Problem: The Number of Seniors and Juniors to Join the Company II
-- Approach: The hiring rule is the same cheapest-first walk as in the first version of this problem, so a running total of salaries in ascending order again marks how far the budget reaches down each list, but here the identities of the hired candidates are wanted rather than their count. Each group's running totals are computed separately, the seniors are resolved first, and the largest affordable senior total is added to every junior's running total so the juniors spend only what is left. Selecting the rows whose running total stays within the budget from each group and unioning them gives the hired ids, with the window framed by rows so the totals stay strictly per-candidate.

WITH senior_running AS (
    SELECT
        employee_id,
        SUM(salary) OVER (
            ORDER BY salary, employee_id
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS spent
    FROM Candidates
    WHERE experience = 'Senior'
),
senior_spend AS (
    SELECT COALESCE(MAX(spent), 0) AS spent
    FROM senior_running
    WHERE spent <= 70000
),
junior_running AS (
    SELECT
        employee_id,
        SUM(salary) OVER (
            ORDER BY salary, employee_id
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS spent
    FROM Candidates
    WHERE experience = 'Junior'
)
SELECT employee_id
FROM senior_running
WHERE spent <= 70000
UNION ALL
SELECT employee_id
FROM junior_running
WHERE spent + (SELECT spent FROM senior_spend) <= 70000;
