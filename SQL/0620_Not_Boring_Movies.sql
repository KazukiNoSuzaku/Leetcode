-- Report movies with odd id and non-boring description, ordered by rating descending.
-- Author: Kaustav Ghosh

SELECT * FROM Cinema
WHERE id % 2 = 1 AND description != 'boring'
ORDER BY rating DESC;
