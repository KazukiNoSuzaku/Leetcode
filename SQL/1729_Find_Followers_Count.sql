-- Author: Kaustav Ghosh
-- Problem: Find Followers Count
-- Approach: The pair of columns is the table's key, so a user can never list the same follower twice and a plain COUNT over the group is already a count of distinct followers; COUNT(DISTINCT ...) would be correct too but would pay for a deduplication the key already guarantees. Users nobody follows simply have no rows and are correctly absent, and the ordering is by user id as asked.

SELECT user_id,
       COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id ASC;
