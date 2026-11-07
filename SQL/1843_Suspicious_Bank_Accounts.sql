-- Author: Kaustav Ghosh
-- Problem: Suspicious Bank Accounts
-- Approach: Only deposits count towards income, so the deposits are grouped per account and per calendar month and compared against that account's ceiling, which leaves one row per month that went over. Turning the month into a single integer, twelve times the year plus the month, makes two months consecutive exactly when their numbers differ by one, which avoids any date arithmetic across a year boundary. Self-joining the offending months on that difference then finds the accounts that went over twice in a row, and DISTINCT collapses an account that did so during several different stretches.

WITH OverLimit AS (
    SELECT
        t.account_id,
        YEAR(t.day) * 12 + MONTH(t.day) AS month_index
    FROM Transactions AS t
    JOIN Accounts AS a
        ON a.account_id = t.account_id
    WHERE t.type = 'Creditor'
    GROUP BY t.account_id, YEAR(t.day) * 12 + MONTH(t.day), a.max_income
    HAVING SUM(t.amount) > a.max_income
)
SELECT DISTINCT earlier.account_id
FROM OverLimit AS earlier
JOIN OverLimit AS later
    ON later.account_id = earlier.account_id
   AND later.month_index = earlier.month_index + 1;
