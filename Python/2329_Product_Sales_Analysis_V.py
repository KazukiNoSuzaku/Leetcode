# Author: Kaustav Ghosh
# Problem: 2329. Product Sales Analysis V
# URL: https://leetcode.com/problems/product-sales-analysis-v/
# Difficulty: Easy
# Note: Premium SQL problem
#
# Approach:
# Join Sales with Users to get the buyer's join date.
# Sum spending per user (quantity * price), then return user_id and total_spending
# sorted by total_spending descending, then user_id ascending.
#
# SQL Solution:
# SELECT s.user_id,
#        SUM(s.quantity * p.price) AS spending
# FROM Sales s
# JOIN Product p ON s.product_id = p.product_id
# GROUP BY s.user_id
# ORDER BY spending DESC, s.user_id ASC;

class Solution(object):
    pass
