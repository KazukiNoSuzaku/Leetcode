# Author: Kaustav Ghosh
# Premium problem - Products Price for Each Store
# SQL: Pivot table using CASE WHEN to get price for each store
# SELECT product_id,
#        SUM(CASE WHEN store = 'store1' THEN price END) AS store1,
#        SUM(CASE WHEN store = 'store2' THEN price END) AS store2,
#        SUM(CASE WHEN store = 'store3' THEN price END) AS store3
# FROM Products
# GROUP BY product_id;

class Solution(object):
    pass
