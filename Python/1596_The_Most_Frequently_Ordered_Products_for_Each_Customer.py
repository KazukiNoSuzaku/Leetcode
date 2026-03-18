# Author: Kaustav Ghosh
# Problem: 1596 - The Most Frequently Ordered Products for Each Customer (Premium SQL)
# Approach: GROUP BY customer and product, rank by count, keep max count per customer

# SQL Solution (Premium Problem):
# SELECT o.customer_id, o.product_id, p.product_name
# FROM (
#     SELECT customer_id, product_id,
#            RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(*) DESC) AS rnk
#     FROM Orders
#     GROUP BY customer_id, product_id
# ) o
# JOIN Products p ON o.product_id = p.product_id
# WHERE o.rnk = 1;

class Solution(object):
    pass
