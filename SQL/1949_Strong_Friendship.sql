-- Author: Kaustav Ghosh
-- Problem: Strong Friendship
-- Approach: The stored rows only list each friendship once, with the smaller id first, so asking "who are this user's friends" needs both directions; a union of the table with its own columns swapped gives a plain person-to-friend list to look things up in. Every candidate pair is then just a row of the original table, which already satisfies user1_id < user2_id and so cannot produce a duplicate or a reversed copy, and joining the friend list once per side and matching the friend column counts the friends the two have in common. Grouping by the pair and keeping groups of at least three gives the strong friendships; a user can never show up as their own common friend because that would require a row saying someone is friends with themselves.

WITH Both AS (
    SELECT user1_id AS person, user2_id AS friend FROM Friendship
    UNION ALL
    SELECT user2_id AS person, user1_id AS friend FROM Friendship
)
SELECT
    f.user1_id,
    f.user2_id,
    COUNT(*) AS common_friend
FROM Friendship AS f
JOIN Both AS a ON a.person = f.user1_id
JOIN Both AS b ON b.person = f.user2_id AND b.friend = a.friend
GROUP BY f.user1_id, f.user2_id
HAVING COUNT(*) >= 3;
