-- Find the name of the winning candidate (the one who received the most votes).
-- Author: Kaustav Ghosh

SELECT name
FROM Candidate
WHERE id = (
    SELECT candidateId
    FROM Vote
    GROUP BY candidateId
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
