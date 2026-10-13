-- Author: Kaustav Ghosh
-- Problem: Customer Who Visited but Did Not Make Any Transactions
-- Approach: A visit is empty when the join to Transactions finds nothing, so a LEFT JOIN keeps every visit and leaves the transaction columns NULL exactly for the empty ones; filtering on a NULL transaction_id therefore selects those visits, and counting them per customer gives how many times each customer came without buying. The count must be over visits rather than over the joined rows, but since each surviving row is one visit with no match, a plain COUNT(*) is already per-visit.

SELECT v.customer_id,
       COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
