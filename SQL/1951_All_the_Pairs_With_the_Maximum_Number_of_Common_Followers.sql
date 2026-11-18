-- Author: Kaustav Ghosh
-- Problem: All the Pairs With the Maximum Number of Common Followers
-- Approach: Two users share a follower whenever the same follower_id appears in a row for each of them, so joining Relations to itself on follower_id and grouping by the pair of users counts their common followers directly. Requiring the first user's id to be strictly smaller than the second's does three jobs at once: it fixes the output orientation the problem asks for, it stops a pair appearing twice in both orders, and it keeps a user from being paired with themselves. The maximum count is then read back off that same grouped result in a subquery, and every pair matching it is returned, which is what makes ties all come through rather than just one of them.

WITH Common AS (
    SELECT
        r1.user_id AS user1_id,
        r2.user_id AS user2_id,
        COUNT(*) AS followers
    FROM Relations AS r1
    JOIN Relations AS r2
        ON r2.follower_id = r1.follower_id
        AND r1.user_id < r2.user_id
    GROUP BY r1.user_id, r2.user_id
)
SELECT user1_id, user2_id
FROM Common
WHERE followers = (SELECT MAX(followers) FROM Common);
