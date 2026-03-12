-- Author: Kaustav Ghosh
-- Count unique comments per post (posts are submissions with no parent)

SELECT s.sub_id AS post_id,
       COUNT(DISTINCT c.sub_id) AS number_of_comments
FROM Submissions s
LEFT JOIN Submissions c ON s.sub_id = c.parent_id
WHERE s.parent_id IS NULL
GROUP BY s.sub_id
ORDER BY post_id;
