-- Author: Kaustav Ghosh
-- Problem: Replace Employee ID With The Unique Identifier
-- Approach: LEFT JOIN Employees with EmployeeUNI

SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;
