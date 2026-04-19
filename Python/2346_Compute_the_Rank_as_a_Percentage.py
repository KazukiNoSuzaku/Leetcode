# Author: Kaustav Ghosh
# 2346. Compute the Rank as a Percentage
# https://leetcode.com/problems/compute-the-rank-as-a-percentage/
# Difficulty: Medium (Premium)
#
# SQL Solution:
# SELECT student_id, department_id,
#        ROUND(
#            (RANK() OVER (PARTITION BY department_id ORDER BY mark DESC) - 1) * 100.0
#            / (COUNT(*) OVER (PARTITION BY department_id) - 1),
#            2
#        ) AS percentage
# FROM Students;
#
# Use RANK() to get each student's rank within their department,
# then express as a percentage of total students in that department.

class Solution(object):
    pass
