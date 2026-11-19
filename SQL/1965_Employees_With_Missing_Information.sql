-- Author: Kaustav Ghosh
-- Problem: Employees With Missing Information
-- Approach: An employee is incomplete exactly when their id appears in one table but not the other, so the answer is the symmetric difference of the two id sets. I take the ids in Employees with no matching row in Salaries, take the ids in Salaries with no matching row in Employees, and combine them with UNION, which also removes any duplicate ids although each table already has unique ids. The problem asks for ascending order, so the ordering is stated explicitly rather than relying on how the engine happens to return the rows.

SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
