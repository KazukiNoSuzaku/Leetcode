-- Author: Kaustav Ghosh
-- Problem: The Latest Login in 2020
-- Approach: Restricting to 2020 before grouping is what makes this a plain aggregate: the filter keeps only that year's logins, so the largest remaining timestamp per user is already the answer, and a user with no login in 2020 contributes no rows and so disappears from the output without needing an explicit exclusion. Filtering on the year rather than comparing against a date range keeps the condition a single predicate.

SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;
