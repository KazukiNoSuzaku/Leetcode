-- Author: Kaustav Ghosh
-- Problem: The Number of Seniors and Juniors to Join the Company
-- Approach: Hiring as many people as possible from a group on a fixed budget means taking them cheapest first, so a running total of salaries in ascending order tells us exactly how far down each list the budget reaches: everyone whose running total still fits is hired. The window is framed by rows rather than by value, because salaries may tie and a value-framed total would lump tied candidates together and report the same inflated total for all of them, understating how many fit. The seniors are settled first and the largest affordable senior total becomes the juniors' starting spend, so the two criteria are applied in the order the statement demands, and both groups are reported even when nobody is hired.

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
senior_hired AS (
    SELECT
        COUNT(*) AS hired,
        COALESCE(MAX(spent), 0) AS spent
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
SELECT
    'Senior' AS experience,
    (SELECT hired FROM senior_hired) AS accepted_candidates
UNION ALL
SELECT
    'Junior' AS experience,
    (
        SELECT COUNT(*)
        FROM junior_running
        WHERE spent + (SELECT spent FROM senior_hired) <= 70000
    ) AS accepted_candidates;
