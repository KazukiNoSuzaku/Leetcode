-- Author: Kaustav Ghosh
-- Problem: Accepted Candidates From the Interviews
-- Approach: The two requirements live in different tables, so the candidates are joined to their interview rounds on the shared interview identifier and then grouped back to one row per candidate. Experience belongs to the candidate rather than to any round, so it is filtered before grouping, which discards those rows as early as possible; the score requirement is a property of the group and so belongs in a HAVING clause over the summed round scores. The join is an inner one, which drops a candidate whose interview recorded no rounds at all, and that costs nothing here because such a candidate totals zero and could never clear the threshold anyway.

SELECT c.candidate_id
FROM Candidates AS c
JOIN Rounds AS r ON r.interview_id = c.interview_id
WHERE c.years_of_exp >= 2
GROUP BY c.candidate_id
HAVING SUM(r.score) > 15;
