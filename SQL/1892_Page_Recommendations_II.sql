-- Author: Kaustav Ghosh
-- Problem: Page Recommendations II
-- Approach: Friendship is stored once per pair but has to be read in both directions, so the table is first unfolded into one row per user per friend. Joining that to the pages those friends like produces every candidate recommendation, and grouping by user and page counts how many distinct friends like it, which is a plain row count because a friend can appear at most once per page. Pages the user already likes are excluded with a correlated NOT EXISTS rather than an anti-join, which keeps the count untouched and cannot duplicate rows.

WITH Friends AS (
    SELECT user1_id AS user_id, user2_id AS friend_id FROM Friendship
    UNION ALL
    SELECT user2_id AS user_id, user1_id AS friend_id FROM Friendship
)
SELECT
    f.user_id,
    l.page_id,
    COUNT(*) AS friends_likes
FROM Friends AS f
JOIN Likes AS l
    ON l.user_id = f.friend_id
WHERE NOT EXISTS (
    SELECT 1
    FROM Likes AS own
    WHERE own.user_id = f.user_id
      AND own.page_id = l.page_id
)
GROUP BY f.user_id, l.page_id;
