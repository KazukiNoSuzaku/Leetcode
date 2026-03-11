-- Select all employees with a bonus less than 1000.
-- Author: Kaustav Ghosh

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
