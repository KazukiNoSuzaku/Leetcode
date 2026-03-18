-- Author: Kaustav Ghosh
-- Problem: 1581 - Customer Who Visited but Did Not Make Any Transaction
-- Approach: LEFT JOIN on visit_id, WHERE transaction IS NULL, count per customer

SELECT customer_id, COUNT(visit_id) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (
    SELECT visit_id FROM Transactions
)
GROUP BY customer_id;
