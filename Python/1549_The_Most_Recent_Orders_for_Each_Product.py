# Author: Kaustav Ghosh
# Problem: 1549 - The Most Recent Orders for Each Product (Premium SQL)
# Approach: ROW_NUMBER partition by product_id, filter rn = 1

# SQL Solution (Premium Problem):
# SELECT p.product_name, o.product_id, o.order_id, o.order_date
# FROM Products p
# JOIN (
#     SELECT *, ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY order_date DESC) AS rn
#     FROM Orders
# ) o ON p.product_id = o.product_id
# WHERE o.rn = 1
# ORDER BY p.product_name, o.product_id, o.order_id;

class Solution(object):
    pass
