-- Author: Kaustav Ghosh
-- Problem: Bank Account Summary
-- Approach: Total what each user sent and what they received in two grouped subqueries, then left join both onto Users so people with no transactions keep their starting credit. The balance is credit plus receipts minus payments, and a negative balance flags the breach

SELECT u.user_id,
       u.user_name,
       u.credit + COALESCE(received.total, 0) - COALESCE(sent.total, 0) AS credit,
       CASE WHEN u.credit + COALESCE(received.total, 0) - COALESCE(sent.total, 0) < 0
            THEN 'Yes' ELSE 'No' END AS credit_limit_breached
FROM Users u
LEFT JOIN (SELECT paid_to AS user_id, SUM(amount) AS total
           FROM Transactions GROUP BY paid_to) received
       ON received.user_id = u.user_id
LEFT JOIN (SELECT paid_by AS user_id, SUM(amount) AS total
           FROM Transactions GROUP BY paid_by) sent
       ON sent.user_id = u.user_id;
