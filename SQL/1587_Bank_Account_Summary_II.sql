-- Author: Kaustav Ghosh
-- Problem: 1587 - Bank Account Summary II
-- Approach: GROUP BY account, HAVING SUM > 10000

SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;
