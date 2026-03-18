# Author: Kaustav Ghosh
# Problem: 1511 - Customer Order Frequency (Premium SQL)
# Approach: HAVING SUM for June/July spending >= 100

# SQL Solution (Premium Problem):
# SELECT c.customer_id, c.name
# FROM Customers c
# JOIN Orders o ON c.customer_id = o.customer_id
# JOIN Product p ON o.product_id = p.product_id
# GROUP BY c.customer_id, c.name
# HAVING
#   SUM(CASE WHEN DATE_FORMAT(o.order_date, '%Y-%m') = '2020-06' THEN o.quantity * p.price ELSE 0 END) >= 100
#   AND SUM(CASE WHEN DATE_FORMAT(o.order_date, '%Y-%m') = '2020-07' THEN o.quantity * p.price ELSE 0 END) >= 100;

class Solution(object):
    pass
