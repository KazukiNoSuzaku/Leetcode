-- Author: Kaustav Ghosh
-- Problem: Countries You Can Safely Invest In
-- Approach: A call belongs to the country of each participant, so join Calls to Person on either side of the call; grouping by country then averages every call that touched it, and HAVING compares it with the global average

SELECT c.name AS country
FROM Person p
JOIN Country c ON SUBSTRING(p.phone_number, 1, 3) = c.country_code
JOIN Calls l ON p.id = l.caller_id OR p.id = l.callee_id
GROUP BY c.name
HAVING AVG(l.duration) > (SELECT AVG(duration) FROM Calls);
