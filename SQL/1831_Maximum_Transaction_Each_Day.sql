-- Author: Kaustav Ghosh
-- Problem: Maximum Transaction Each Day
-- Approach: The day column carries a time as well, so the grouping key has to be the date part alone, otherwise every transaction would land in its own group. One aggregate pass finds the largest amount per date, and joining the original rows back to that result on both the date and the amount keeps every transaction tied for the daily maximum rather than an arbitrary one, which is what the problem asks for. The join is on equality to a value that was itself drawn from the table, so a day's rows cannot be duplicated beyond the genuine ties.

SELECT t.transaction_id
FROM Transactions AS t
JOIN (
    SELECT DATE(day) AS on_day, MAX(amount) AS top_amount
    FROM Transactions
    GROUP BY DATE(day)
) AS peak
    ON DATE(t.day) = peak.on_day
   AND t.amount = peak.top_amount
ORDER BY t.transaction_id;
