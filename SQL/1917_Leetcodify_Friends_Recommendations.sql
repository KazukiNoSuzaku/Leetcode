-- Author: Kaustav Ghosh
-- Problem: Leetcodify Friends Recommendations
-- Approach: Two users qualify when they share at least three different songs on one shared day, so Listens is joined to itself on day and song between distinct users and grouped per ordered pair per day. The count must be over distinct songs rather than rows, because Listens is explicitly allowed to hold duplicate rows and a single song played twice would otherwise count twice. Grouping includes the day so that songs shared across different days never add up, and the outer DISTINCT then collapses a pair that qualifies on several days into one recommendation. Existing friendships are removed afterwards, testing both column orders since the friendship table stores each pair only once.

SELECT DISTINCT pair.user_id, pair.recommended_id
FROM (
    SELECT
        mine.user_id AS user_id,
        theirs.user_id AS recommended_id
    FROM Listens AS mine
    JOIN Listens AS theirs
        ON theirs.day = mine.day
       AND theirs.song_id = mine.song_id
       AND theirs.user_id <> mine.user_id
    GROUP BY mine.user_id, theirs.user_id, mine.day
    HAVING COUNT(DISTINCT mine.song_id) >= 3
) AS pair
WHERE NOT EXISTS (
    SELECT 1
    FROM Friendship AS f
    WHERE (f.user1_id = pair.user_id AND f.user2_id = pair.recommended_id)
       OR (f.user1_id = pair.recommended_id AND f.user2_id = pair.user_id)
);
