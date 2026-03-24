# Author: Kaustav Ghosh
# Problem 2084: Drop Type 1 Orders for Customers With Type 0 Orders (Premium)
# SQL Solution:
# SELECT * FROM Orders
# WHERE customer_id NOT IN (
#     SELECT customer_id FROM Orders WHERE order_type = 0
# ) OR order_type = 0;

class Solution(object):
    pass
