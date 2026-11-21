-- Author: Kaustav Ghosh
-- Problem: Find Cutoff Score for Each School
-- Approach: A score is usable for a school when the number of students who reached it does not exceed the school's capacity, so joining the two tables on that single inequality collects exactly the usable scores per school. Among those, the two stated goals agree rather than compete: the student count never rises as the score rises, so the smallest usable score is also the one admitting the most applicants, and taking the minimum score per school satisfies "maximise the applicants" and "break ties by the smallest score" at once. The join has to be a left join so a school with no usable score still produces a row, and COALESCE turns that row's missing score into the required -1.

SELECT
    s.school_id,
    COALESCE(MIN(e.score), -1) AS score
FROM Schools AS s
LEFT JOIN Exam AS e ON e.student_count <= s.capacity
GROUP BY s.school_id;
