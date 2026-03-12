-- Premium problem - not available without subscription
-- Author: Kaustav Ghosh
-- Typical approach: Combine approved transactions and chargebacks by month/country

SELECT month, country,
       SUM(CASE WHEN type = 'approved' THEN 1 ELSE 0 END) AS approved_count,
       SUM(CASE WHEN type = 'approved' THEN amount ELSE 0 END) AS approved_amount,
       SUM(CASE WHEN type = 'chargeback' THEN 1 ELSE 0 END) AS chargeback_count,
       SUM(CASE WHEN type = 'chargeback' THEN amount ELSE 0 END) AS chargeback_amount
FROM (
    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, amount, 'approved' AS type
    FROM Transactions WHERE state = 'approved'
    UNION ALL
    SELECT DATE_FORMAT(c.trans_date, '%Y-%m') AS month, t.country, t.amount, 'chargeback' AS type
    FROM Chargebacks c JOIN Transactions t ON c.trans_id = t.id
) combined
GROUP BY month, country;
