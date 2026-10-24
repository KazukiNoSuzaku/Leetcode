-- Author: Kaustav Ghosh
-- Problem: Number of Calls Between Two Persons
-- Approach: A call between two people is the same relationship whichever way round it was placed, so the two endpoints are first normalised with the smaller id as person1 and the larger as person2; that single step is what collapses a pair's calls in both directions into one group. Grouping on those normalised expressions then counts the calls and totals the durations, and the table is allowed duplicate rows, which is correct here because two identical calls genuinely are two calls and so must both be counted.

SELECT LEAST(from_id, to_id) AS person1,
       GREATEST(from_id, to_id) AS person2,
       COUNT(*) AS call_count,
       SUM(duration) AS total_duration
FROM Calls
GROUP BY LEAST(from_id, to_id), GREATEST(from_id, to_id);
