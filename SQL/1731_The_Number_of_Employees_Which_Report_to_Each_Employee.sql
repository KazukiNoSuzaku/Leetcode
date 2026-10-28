-- Author: Kaustav Ghosh
-- Problem: The Number of Employees Which Report to Each Employee
-- Approach: Managers and reports live in the same table, so it is joined to itself with one copy acting as the manager and the other as the report, matched on the report's reports_to. Using an inner join is what defines a manager here: anyone with nobody pointing at them produces no joined rows and so is correctly left out, which is exactly the problem's definition of at least one direct report, and it also disposes of the employees whose reports_to is NULL without a separate filter. Grouping on the manager then yields both the count and the average age, rounded to a whole number as asked.

SELECT m.employee_id,
       m.name,
       COUNT(e.employee_id) AS reports_count,
       ROUND(AVG(e.age)) AS average_age
FROM Employees m
JOIN Employees e ON e.reports_to = m.employee_id
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;
