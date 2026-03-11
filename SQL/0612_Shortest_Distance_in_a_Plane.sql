-- Find the shortest distance between any two points in the Point2D table.
-- Author: Kaustav Ghosh

SELECT ROUND(MIN(SQRT(POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2))), 2) AS shortest
FROM Point2D p1
JOIN Point2D p2 ON (p1.x, p1.y) < (p2.x, p2.y);
