# Author: Kaustav Ghosh
# Problem 2041: Accepted Candidates From the Interviews (Premium)
# SQL Problem:
# SELECT c.candidate_id
# FROM Candidates c
# JOIN Rounds r ON c.interview_id = r.interview_id
# WHERE c.years_of_exp >= 2
# GROUP BY c.candidate_id
# HAVING SUM(r.score) > 15;

class Solution(object):
    pass
