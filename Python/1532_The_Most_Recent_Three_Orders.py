# Author: Kaustav Ghosh
# Problem: 1532 - The Most Recent Three Orders (Premium SQL)
# Approach: ROW_NUMBER per customer ordered by order_date DESC, filter <= 3

# SQL Solution (Premium Problem):
# SELECT c.name AS customer_name, c.customer_id, o.order_id, o.order_date
# FROM Customers c
# JOIN (
#     SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
#     FROM Orders
# ) o ON c.customer_id = o.customer_id
# WHERE o.rn <= 3
# ORDER BY c.name, c.customer_id, o.order_date DESC;

class Solution(object):
    pass
