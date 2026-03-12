-- Author: Kaustav Ghosh
-- Find viewers who viewed more than one article on the same day

SELECT DISTINCT viewer_id AS id
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1
ORDER BY id;
