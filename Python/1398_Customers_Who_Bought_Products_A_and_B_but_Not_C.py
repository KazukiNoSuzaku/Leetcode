# Author: Kaustav Ghosh
# Problem: Customers Who Bought Products A and B but Not C (Premium SQL)
# Approach: GROUP BY customer with HAVING conditions on product names
#
# SQL Solution:
# SELECT c.customer_id, c.customer_name
# FROM Customers c
# JOIN Orders o ON c.customer_id = o.customer_id
# GROUP BY c.customer_id, c.customer_name
# HAVING SUM(o.product_name = 'A') > 0
#    AND SUM(o.product_name = 'B') > 0
#    AND SUM(o.product_name = 'C') = 0
# ORDER BY c.customer_id

class Solution(object):
    pass
