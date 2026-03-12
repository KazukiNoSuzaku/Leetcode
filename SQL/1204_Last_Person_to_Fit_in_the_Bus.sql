-- Author: Kaustav Ghosh
-- Find the last person who can board without exceeding 1000 weight limit

SELECT person_name
FROM (
    SELECT person_name,
           SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) t
WHERE cumulative_weight <= 1000
ORDER BY cumulative_weight DESC
LIMIT 1;
