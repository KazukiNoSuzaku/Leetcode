-- Author: Kaustav Ghosh
-- Problem: Bank Account Summary II
-- Approach: Amounts are already signed, with deposits positive and transfers negative, so a balance is just their sum per account and no CASE expression is needed. Joining Users brings in the name, grouping by the account aggregates that user's transactions, and the threshold has to sit in HAVING rather than WHERE because it tests the aggregate rather than an individual row. An inner join is enough: an account with no transactions has a balance of zero and could never clear 10000.

SELECT u.name,
       SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY t.account, u.name
HAVING SUM(t.amount) > 10000;
