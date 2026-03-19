# Author: Kaustav Ghosh
# https://leetcode.com/problems/products-worth-over-invoices/
# Premium SQL Problem
#
# SELECT p.name,
#        IFNULL(SUM(i.rest), 0) AS rest,
#        IFNULL(SUM(i.paid), 0) AS paid,
#        IFNULL(SUM(i.canceled), 0) AS canceled,
#        IFNULL(SUM(i.refunded), 0) AS refunded
# FROM Product p
# LEFT JOIN Invoice i ON p.product_id = i.product_id
# GROUP BY p.name
# ORDER BY p.name;

class Solution(object):
    pass
