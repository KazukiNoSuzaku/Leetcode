# Author: Kaustav Ghosh
# Problem: 2324. Product Sales Analysis IV
# URL: https://leetcode.com/problems/product-sales-analysis-iv/
# Difficulty: Medium
# Note: Premium SQL problem
#
# Approach:
# For each user, find the product(s) they spent the most on (total price * quantity).
# Use a subquery/window function to rank products per user by total spend descending,
# then select those ranked first.
#
# SQL Solution:
# WITH spend AS (
#     SELECT s.user_id, s.product_id,
#            SUM(s.quantity * p.price) AS total_spend
#     FROM Sales s
#     JOIN Product p ON s.product_id = p.product_id
#     GROUP BY s.user_id, s.product_id
# ),
# ranked AS (
#     SELECT user_id, product_id,
#            RANK() OVER (PARTITION BY user_id ORDER BY total_spend DESC) AS rnk
#     FROM spend
# )
# SELECT user_id, product_id
# FROM ranked
# WHERE rnk = 1;

class Solution(object):
    pass
