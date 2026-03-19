# Author: Kaustav Ghosh
# https://leetcode.com/problems/hopper-company-queries-i/
# Premium SQL Problem
#
# WITH RECURSIVE months AS (
#     SELECT 1 AS month
#     UNION ALL
#     SELECT month + 1 FROM months WHERE month < 12
# ),
# active_drivers AS (
#     SELECT month, COUNT(*) OVER (ORDER BY month) AS active_drivers
#     FROM months
#     LEFT JOIN Drivers ON YEAR(join_date) < 2020 OR (YEAR(join_date) = 2020 AND MONTH(join_date) <= month)
# ),
# accepted AS (
#     SELECT MONTH(requested_at) AS month, COUNT(*) AS accepted_rides
#     FROM Rides r JOIN AcceptedRides a ON r.ride_id = a.ride_id
#     WHERE YEAR(requested_at) = 2020
#     GROUP BY MONTH(requested_at)
# )
# SELECT m.month, IFNULL(ad.active_drivers, 0), IFNULL(a.accepted_rides, 0)
# FROM months m LEFT JOIN active_drivers ad ON m.month = ad.month
# LEFT JOIN accepted a ON m.month = a.month;

class Solution(object):
    pass
