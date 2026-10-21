-- Author: Kaustav Ghosh
-- Problem: Hopper Company Queries III
-- Approach: Each window divides by three regardless of how many of its months actually had rides, so a month with no activity must still exist as a zero row rather than be absent; the twelve months therefore come from a recursive CTE and the ride totals are left joined onto them with COALESCE. With all twelve rows present and ordered, a window frame of the current row plus the two following gives exactly the three-month span, and I divide that sum by 3.0 explicitly rather than using AVG, which keeps the stated definition visible and keeps the arithmetic out of integer division. Months eleven and twelve are computed but dropped at the end, since their windows would run past December.

WITH RECURSIVE months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1 FROM months WHERE month < 12
),
monthly AS (
    SELECT MONTH(r.requested_at) AS month,
           SUM(a.ride_distance) AS distance,
           SUM(a.ride_duration) AS duration
    FROM Rides r
    JOIN AcceptedRides a ON a.ride_id = r.ride_id
    WHERE YEAR(r.requested_at) = 2020
    GROUP BY MONTH(r.requested_at)
),
filled AS (
    SELECT m.month,
           COALESCE(mo.distance, 0) AS distance,
           COALESCE(mo.duration, 0) AS duration
    FROM months m
    LEFT JOIN monthly mo ON mo.month = m.month
),
windowed AS (
    SELECT month,
           ROUND(SUM(distance) OVER (ORDER BY month
                 ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) / 3.0, 2) AS average_ride_distance,
           ROUND(SUM(duration) OVER (ORDER BY month
                 ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) / 3.0, 2) AS average_ride_duration
    FROM filled
)
SELECT month, average_ride_distance, average_ride_duration
FROM windowed
WHERE month <= 10
ORDER BY month ASC;
