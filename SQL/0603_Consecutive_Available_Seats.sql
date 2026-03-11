-- Find all the consecutive available seats in a cinema.
-- Author: Kaustav Ghosh

SELECT DISTINCT a.seat_id
FROM Cinema a
JOIN Cinema b ON ABS(a.seat_id - b.seat_id) = 1
WHERE a.free = 1 AND b.free = 1
ORDER BY a.seat_id;
