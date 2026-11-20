-- Author: Kaustav Ghosh
-- Problem: Employees Whose Manager Left the Company
-- Approach: A manager who left is one whose own row is gone, so their id survives only in their reports' manager_id and matches no employee_id; that makes the test a self anti-join against the table's own primary key. I use NOT IN against the set of employee ids, which is safe here because employee_id is the primary key and therefore never NULL, so the subquery cannot produce the NULL that would make NOT IN return nothing. Employees with no manager at all must be excluded too, which is handled by requiring manager_id to be present, since a NULL manager_id means nobody left rather than a missing manager. The salary condition is a plain filter, and the ordering the problem asks for is stated explicitly.

SELECT employee_id
FROM Employees
WHERE salary < 30000
    AND manager_id IS NOT NULL
    AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
