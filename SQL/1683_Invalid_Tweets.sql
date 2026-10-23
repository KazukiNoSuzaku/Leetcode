-- Author: Kaustav Ghosh
-- Problem: Invalid Tweets
-- Approach: A single filter on the content's length, using CHAR_LENGTH rather than LENGTH because the question is about the number of characters while LENGTH reports bytes, and the two part company the moment any character is multi-byte. The content here is stated to be alphanumeric, spaces and exclamation marks, so they would agree in practice, but counting characters is what was asked. The comparison is strict, since a tweet of exactly fifteen characters is still valid.

SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
