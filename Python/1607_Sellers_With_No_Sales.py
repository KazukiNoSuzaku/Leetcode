# Author: Kaustav Ghosh
# Problem: 1607 - Sellers With No Sales (Premium SQL)
# Approach: LEFT JOIN Orders, WHERE order IS NULL, filter by year 2020

# SQL Solution (Premium Problem):
# SELECT seller_name
# FROM Seller
# WHERE seller_id NOT IN (
#     SELECT DISTINCT seller_id
#     FROM Orders
#     WHERE YEAR(sale_date) = 2020
# )
# ORDER BY seller_name;

class Solution(object):
    pass
