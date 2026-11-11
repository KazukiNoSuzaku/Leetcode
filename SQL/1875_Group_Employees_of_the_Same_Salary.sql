-- Author: Kaustav Ghosh
-- Problem: Group Employees of the Same Salary
-- Approach: Only salaries shared by at least two employees form a team, so those salaries are identified first by a grouped count and the employees on a unique salary are filtered away. The team number is then the rank of the salary among the surviving ones, and DENSE_RANK is the right ranking because every employee sharing a salary must receive the same number and the numbering must not skip ahead where a team has several members. Filtering before ranking is what keeps the discarded unique salaries out of the numbering.

SELECT
    employee_id,
    name,
    salary,
    DENSE_RANK() OVER (ORDER BY salary) AS team_id
FROM Employees
WHERE salary IN (
    SELECT salary
    FROM Employees
    GROUP BY salary
    HAVING COUNT(*) > 1
)
ORDER BY team_id, employee_id;
