-- Author: Kaustav Ghosh
-- Problem: Count Salary Categories
-- Approach: All three categories must appear even when nothing falls into them, which rules out grouping the accounts by a derived category because an empty group produces no row at all. Instead each category is its own aggregate over a filtered set, and COUNT with no GROUP BY still returns a single row holding zero when the filter matches nothing, so stacking the three with UNION ALL guarantees exactly three rows. The boundaries follow the problem exactly: strictly below twenty thousand, inclusive up to fifty thousand, and strictly above.

SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000
UNION ALL
SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income BETWEEN 20000 AND 50000
UNION ALL
SELECT 'High Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000;
