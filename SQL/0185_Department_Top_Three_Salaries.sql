-- Table: Employee (same as 184)
-- Table: Department (same as 184)
-- A company's executives are interested in seeing who earns the most money in each of the
-- company's departments. Write a solution to find the employees who are high earners in
-- each of the departments.
-- A high earner in a department is an employee who has a salary in the top three unique
-- salaries for that department.

-- Author: Kaustav Ghosh

SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId AND e2.salary > e.salary
) < 3;
