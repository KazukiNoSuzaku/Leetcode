-- Author: Kaustav Ghosh
-- Problem: Leetcodify Similar Friends
-- Approach: Only existing friendships are candidates, so Friendship drives the query and each side is joined to its own listening history, matched on the same day and the same song. Grouping per friendship per day and counting distinct songs applies the three-song rule within a single day; counting rows instead would be wrong because Listens may contain duplicates, and leaving the day out of the grouping would let songs from different days accumulate. The outer DISTINCT collapses a pair that qualifies on more than one day, and because the pairs come straight from Friendship they already carry the required ordering with the smaller id first.

SELECT DISTINCT user1_id, user2_id
FROM (
    SELECT f.user1_id, f.user2_id
    FROM Friendship AS f
    JOIN Listens AS first
        ON first.user_id = f.user1_id
    JOIN Listens AS second
        ON second.user_id = f.user2_id
       AND second.day = first.day
       AND second.song_id = first.song_id
    GROUP BY f.user1_id, f.user2_id, first.day
    HAVING COUNT(DISTINCT first.song_id) >= 3
) AS similar;
