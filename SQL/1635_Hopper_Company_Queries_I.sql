-- Author: Kaustav Ghosh
-- Problem: Hopper Company Queries I
-- Approach: Every month of 2020 must appear even when nothing happened in it, so the twelve months cannot come from the data and are manufactured by a recursive CTE instead; everything else is then left joined onto that skeleton. Active drivers are cumulative rather than per month, so the count is a correlated subquery over everyone who had joined by the end of that month, which means anyone hired before 2020 at all plus anyone hired in 2020 up to and including that month, while 2021 hires are excluded. Accepted rides are counted per month from the join of Rides to AcceptedRides, since Rides alone holds the request date and AcceptedRides alone says the ride happened, and COALESCE turns a month with no matching rides into zero rather than NULL.

WITH RECURSIVE months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1 FROM months WHERE month < 12
),
monthly_rides AS (
    SELECT MONTH(r.requested_at) AS month, COUNT(*) AS rides
    FROM Rides r
    JOIN AcceptedRides a ON a.ride_id = r.ride_id
    WHERE YEAR(r.requested_at) = 2020
    GROUP BY MONTH(r.requested_at)
)
SELECT m.month,
       (SELECT COUNT(*)
        FROM Drivers d
        WHERE YEAR(d.join_date) < 2020
           OR (YEAR(d.join_date) = 2020 AND MONTH(d.join_date) <= m.month)) AS active_drivers,
       COALESCE(mr.rides, 0) AS accepted_rides
FROM months m
LEFT JOIN monthly_rides mr ON mr.month = m.month
ORDER BY m.month ASC;
