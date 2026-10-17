-- Author: Kaustav Ghosh
-- Problem: Find the Missing IDs
-- Approach: The answer is about rows that do not exist, so there is nothing in the table to select and the candidate numbers have to be manufactured first; a recursive CTE counts from one to a hundred, which the problem guarantees covers every possible id. From that universe I drop the ids that are present and anything above the largest id present, since the range stops there. The NOT IN is safe here because customer_id is the table's unique key and so is never NULL, which is the one case that would make NOT IN collapse to no rows at all.

WITH RECURSIVE candidates AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM candidates WHERE n < 100
)
SELECT c.n AS ids
FROM candidates c
WHERE c.n < (SELECT MAX(customer_id) FROM Customers)
  AND c.n NOT IN (SELECT customer_id FROM Customers)
ORDER BY ids ASC;
