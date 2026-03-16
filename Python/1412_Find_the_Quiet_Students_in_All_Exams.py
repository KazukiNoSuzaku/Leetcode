# Author: Kaustav Ghosh
# Problem: Find the Quiet Students in All Exams (Premium SQL)
# Approach: Find students who never had highest or lowest score in any exam
#
# SQL Solution:
# SELECT DISTINCT s.student_id, s.student_name
# FROM Student s
# JOIN Exam e ON s.student_id = e.student_id
# WHERE s.student_id NOT IN (
#     SELECT student_id FROM Exam e2
#     WHERE score = (SELECT MAX(score) FROM Exam WHERE exam_id = e2.exam_id)
#        OR score = (SELECT MIN(score) FROM Exam WHERE exam_id = e2.exam_id)
# )
# ORDER BY s.student_id

class Solution(object):
    pass
