-- Display the records with three or more rows with consecutive id's, and the number of
-- people is greater than or equal to 100.
-- Author: Kaustav Ghosh

SELECT DISTINCT s1.*
FROM Stadium s1, Stadium s2, Stadium s3
WHERE s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100
AND (
    (s1.id + 1 = s2.id AND s2.id + 1 = s3.id) OR
    (s2.id + 1 = s1.id AND s1.id + 1 = s3.id) OR
    (s2.id + 1 = s3.id AND s3.id + 1 = s1.id)
)
ORDER BY s1.visit_date;
