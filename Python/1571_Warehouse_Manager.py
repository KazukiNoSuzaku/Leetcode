# Author: Kaustav Ghosh
# Problem: 1571 - Warehouse Manager (Premium SQL)
# Approach: Join products with warehouse volumes, sum product volumes per warehouse

# SQL Solution (Premium Problem):
# SELECT w.name AS warehouse_name, SUM(w.units * p.Width * p.Length * p.Height) AS volume
# FROM Warehouse w
# JOIN Products p ON w.product_id = p.product_id
# GROUP BY w.name;

class Solution(object):
    pass
