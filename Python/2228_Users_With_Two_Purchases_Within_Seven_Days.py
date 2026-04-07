# Author: Kaustav Ghosh
# Problem: 2228. Users With Two Purchases Within Seven Days
# URL: https://leetcode.com/problems/users-with-two-purchases-within-seven-days/
# Difficulty: Medium
# Note: Premium SQL problem
#
# SQL Approach:
# Self-join the Purchases table on the same user_id where the two purchase
# dates differ but fall within a 7-day window (0 < date diff <= 7).
# Use DISTINCT to avoid duplicate user entries in the result.
#
# SELECT DISTINCT a.user_id
# FROM Purchases a
# JOIN Purchases b
#   ON a.user_id = b.user_id
#  AND a.purchase_id <> b.purchase_id
#  AND DATEDIFF(b.purchase_date, a.purchase_date) BETWEEN 1 AND 7
# ORDER BY a.user_id;

class Solution(object):
    pass
