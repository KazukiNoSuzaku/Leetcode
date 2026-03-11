-- Find followers who are also following others (second-degree followers).
-- Author: Kaustav Ghosh

SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num
FROM Follow f1
JOIN Follow f2 ON f1.follower = f2.followee
GROUP BY f1.follower
ORDER BY f1.follower;
