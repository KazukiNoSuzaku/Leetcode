# Author: Kaustav Ghosh
# Problem: 2230. The Users That Are Not Banned
# URL: https://leetcode.com/problems/the-users-that-are-not-banned/
# Difficulty: Easy
# Note: Premium SQL problem
#
# SQL Approach:
# Filter the Activity table to only include rows where the user_id is NOT
# in the Banned table, then return the distinct qualifying users.
#
# SELECT DISTINCT user_id
# FROM Activity
# WHERE user_id NOT IN (
#     SELECT user_id FROM Banned
# )
# ORDER BY user_id;

class Solution(object):
    pass
