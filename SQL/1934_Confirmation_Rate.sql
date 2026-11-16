-- Author: Kaustav Ghosh
-- Problem: Confirmation Rate
-- Approach: Every signed-up user must appear in the answer, including those who never requested a confirmation message, so the Signups table drives the query and Confirmations is brought in with a left join. Treating each joined row as a one-or-zero score for "was this request confirmed" turns the rate into a plain average over that user's rows, and the average of two decimal places is what the problem asks for. A user with no requests still produces exactly one joined row, whose action is NULL and so scores zero, which is the required rate of 0.00 for that case without any extra branch.

SELECT
    s.user_id,
    ROUND(AVG(CASE WHEN c.action = 'confirmed' THEN 1.0 ELSE 0.0 END), 2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c ON c.user_id = s.user_id
GROUP BY s.user_id;
