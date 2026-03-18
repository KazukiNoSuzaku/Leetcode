# Author: Kaustav Ghosh
# Problem: 1565 - Unique Orders and Customers Per Month (Premium SQL)
# Approach: GROUP BY month, count distinct orders and customers

# SQL Solution (Premium Problem):
# SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
#        COUNT(order_id) AS order_count,
#        COUNT(DISTINCT customer_id) AS customer_count
# FROM Orders
# WHERE invoice > 20
# GROUP BY DATE_FORMAT(order_date, '%Y-%m');

class Solution(object):
    pass
