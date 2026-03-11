-- Find the median salary of each company.
-- Author: Kaustav Ghosh

SELECT id, company, salary
FROM (
    SELECT id, company, salary,
           ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary, id) AS rn,
           COUNT(*) OVER (PARTITION BY company) AS total
    FROM Employee
) t
WHERE rn BETWEEN total/2.0 AND total/2.0 + 1;
