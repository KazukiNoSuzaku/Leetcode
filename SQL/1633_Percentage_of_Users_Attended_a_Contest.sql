-- Author: Kaustav Ghosh
-- Problem: Percentage of Users Attended a Contest
-- Approach: The denominator is the whole user base rather than anything in the grouped rows, so it comes from an uncorrelated subquery counting Users, evaluated once. The numerator is the registrations per contest, and multiplying by 100.0 rather than 100 forces the division into floating point, since integer division would collapse every percentage to zero. Contests nobody registered for simply do not appear in Register and so are correctly absent, and the ordering puts the busiest contests first with the contest id breaking ties.

SELECT r.contest_id,
       ROUND(COUNT(r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;
