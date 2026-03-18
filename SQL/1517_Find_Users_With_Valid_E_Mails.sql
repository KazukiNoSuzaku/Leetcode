-- Author: Kaustav Ghosh
-- Problem: 1517 - Find Users With Valid E-Mails
-- Approach: REGEXP for valid email format

SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$';
