-- Author: Kaustav Ghosh
-- Problem: Calculate Special Bonus
-- Approach: The bonus is a per-row decision with no aggregation involved, so a single conditional expression carries it: an odd employee_id together with a name that does not begin with 'M' pays the full salary, and everything else pays nothing. Using NOT LIKE with a trailing wildcard tests only the first character, and because every employee must appear in the output the condition lives inside the select list rather than in a WHERE clause.

SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM Employees
ORDER BY employee_id;
