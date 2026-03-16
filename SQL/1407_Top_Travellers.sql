-- Author: Kaustav Ghosh
-- Problem: Top Travellers
-- Approach: LEFT JOIN rides, SUM distance, order by distance desc then name

SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;
