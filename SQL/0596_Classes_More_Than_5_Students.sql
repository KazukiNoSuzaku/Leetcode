-- Find all the classes that have at least 5 students.
-- Author: Kaustav Ghosh

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
