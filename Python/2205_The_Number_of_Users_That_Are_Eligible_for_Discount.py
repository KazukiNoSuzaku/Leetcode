# Author: Kaustav Ghosh
# 2205. The Number of Users That Are Eligible for Discount
# https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/
# Difficulty: Easy (Premium SQL)
#
# SQL Approach (Premium):
# Count distinct users who made at least one purchase between startDate and endDate
# (inclusive) with an amount strictly greater than minAmount.
#
# SELECT COUNT(DISTINCT user_id) AS cnt
# FROM Purchases
# WHERE time_stamp BETWEEN startDate AND endDate
#   AND amount > minAmount;
#
# The problem asks for a stored procedure / parameterized query accepting
# (startDate, endDate, minAmount) and returning the count.

class Solution(object):
    pass
