-- Write an SQL query to find managers with at least five direct reports.
-- Author: Kaustav Ghosh

SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
);
