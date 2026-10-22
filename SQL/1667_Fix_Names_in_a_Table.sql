-- Author: Kaustav Ghosh
-- Problem: Fix Names in a Table
-- Approach: The name is rebuilt from two pieces rather than transformed in place: the first character forced to upper case, and everything from the second character onward forced to lower case. Taking the tail with SUBSTRING from position two, with no length given, runs to the end of the string and so needs no length arithmetic, and it yields an empty string rather than failing on a single-character name.

SELECT user_id,
       CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
