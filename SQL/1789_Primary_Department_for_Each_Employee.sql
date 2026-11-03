-- Author: Kaustav Ghosh
-- Problem: Primary Department for Each Employee
-- Approach: An employee is reported with the department flagged 'Y', except that someone belonging to a single department carries no 'Y' at all and must still be reported with that one department. Both cases are a filter on the same rows, so a single WHERE combines them: the flag being 'Y', or the employee appearing exactly once in the table, which a grouped subquery identifies.

SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
   OR employee_id IN (
       SELECT employee_id
       FROM Employee
       GROUP BY employee_id
       HAVING COUNT(*) = 1
   );
