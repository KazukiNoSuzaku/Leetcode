# Author: Kaustav Ghosh
# Problem 1867: Orders With Maximum Quantity Above Average (Premium)
# SQL Problem - Solution in comments
#
# SELECT order_id
# FROM OrdersDetails
# GROUP BY order_id
# HAVING MAX(quantity) > (
#     SELECT AVG(quantity) FROM OrdersDetails
# );

class Solution(object):
    pass
