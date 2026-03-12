-- Premium problem - not available without subscription
-- Author: Kaustav Ghosh
-- Typical approach: Find pages liked by friends but not by user

SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE user_id IN (
    SELECT user2_id FROM Friendship WHERE user1_id = 1
    UNION
    SELECT user1_id FROM Friendship WHERE user2_id = 1
)
AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1);
