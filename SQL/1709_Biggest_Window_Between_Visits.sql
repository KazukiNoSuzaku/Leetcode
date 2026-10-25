-- Author: Kaustav Ghosh
-- Problem: Biggest Window Between Visits
-- Approach: A gap is defined between consecutive visits of the same user, which is exactly what LEAD over a partition by user ordered by date provides, and giving LEAD a default of the stated today means the final visit's open-ended window is produced by the same expression rather than needing a separate branch or a union. The gaps are then reduced to a maximum per user. Duplicate rows are permitted by the schema and are harmless here: a repeated date yields a gap of zero, which can never win the maximum.

WITH gaps AS (
    SELECT user_id,
           DATEDIFF(
               LEAD(visit_date, 1, '2021-01-01') OVER (
                   PARTITION BY user_id ORDER BY visit_date
               ),
               visit_date
           ) AS window_days
    FROM UserVisits
)
SELECT user_id,
       MAX(window_days) AS biggest_window
FROM gaps
GROUP BY user_id
ORDER BY user_id;
