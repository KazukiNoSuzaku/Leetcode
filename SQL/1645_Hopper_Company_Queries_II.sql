-- Author: Kaustav Ghosh
-- Problem: Hopper Company Queries II
-- Approach: Every month of 2020 has to be reported even when nothing happened, so the twelve months come from a recursive CTE rather than from the data. The denominator is cumulative, counting everyone hired by the end of that month, which is anyone hired before 2020 plus anyone hired in 2020 up to that month, so it goes in its own per-month subquery; the numerator counts distinct drivers who accepted a ride that month, distinct because one driver taking two rides still counts once. The CASE guard is not decoration: the problem asks for zero when no drivers are available, whereas dividing by zero in SQL yields NULL, and multiplying by 100.0 rather than 100 keeps the ratio out of integer division.

WITH RECURSIVE months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1 FROM months WHERE month < 12
),
available AS (
    SELECT m.month,
           (SELECT COUNT(*)
            FROM Drivers d
            WHERE YEAR(d.join_date) < 2020
               OR (YEAR(d.join_date) = 2020 AND MONTH(d.join_date) <= m.month)) AS drivers
    FROM months m
),
working AS (
    SELECT MONTH(r.requested_at) AS month,
           COUNT(DISTINCT a.driver_id) AS drivers
    FROM Rides r
    JOIN AcceptedRides a ON a.ride_id = r.ride_id
    WHERE YEAR(r.requested_at) = 2020
    GROUP BY MONTH(r.requested_at)
)
SELECT av.month,
       ROUND(CASE WHEN av.drivers = 0 THEN 0
                  ELSE COALESCE(w.drivers, 0) * 100.0 / av.drivers END, 2) AS working_percentage
FROM available av
LEFT JOIN working w ON w.month = av.month
ORDER BY av.month ASC;
