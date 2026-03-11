-- Find the cumulative sum of an employee's salary over a period of 3 months.
-- Author: Kaustav Ghosh

SELECT e1.id, e1.month,
       SUM(e2.salary) AS salary
FROM Employee e1
JOIN Employee e2 ON e1.id = e2.id AND e2.month BETWEEN e1.month - 2 AND e1.month
WHERE (e1.id, e1.month) NOT IN (
    SELECT id, MAX(month) FROM Employee GROUP BY id
)
GROUP BY e1.id, e1.month
ORDER BY e1.id, e1.month DESC;
