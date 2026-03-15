# SQL problem - Find products with at least 100 units ordered in February 2020.

# Author: Kaustav Ghosh

# SQL solution:
# SELECT p.product_name, SUM(o.unit) AS unit
# FROM Products p
# JOIN Orders o ON p.product_id = o.product_id
# WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
# GROUP BY p.product_id, p.product_name
# HAVING SUM(o.unit) >= 100;

class Solution(object):
    pass
