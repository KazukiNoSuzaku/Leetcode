-- Author: Kaustav Ghosh
-- Problem: All Valid Triplets That Can Represent a Country
-- Approach: Every combination of one student per school is a candidate, which is exactly a three-way cross join, and the only work left is discarding the combinations that clash. Pairwise distinctness has to be spelled out for all three pairs on both the id and the name, because a triplet can clash on just one pair while the other two are fine; checking only consecutive pairs would let a clash between the first and third student slip through, which is precisely the case the problem's own example rejects.

SELECT a.student_name AS member_A,
       b.student_name AS member_B,
       c.student_name AS member_C
FROM SchoolA a
CROSS JOIN SchoolB b
CROSS JOIN SchoolC c
WHERE a.student_id <> b.student_id
  AND b.student_id <> c.student_id
  AND a.student_id <> c.student_id
  AND a.student_name <> b.student_name
  AND b.student_name <> c.student_name
  AND a.student_name <> c.student_name;
