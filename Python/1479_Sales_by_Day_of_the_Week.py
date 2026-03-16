# Author: Kaustav Ghosh
# Problem: Sales by Day of the Week (Premium SQL)
# Approach: Pivot sales quantity by day of week using CASE WHEN
#
# SQL Solution:
# SELECT i.item_category AS Category,
#        SUM(CASE WHEN DAYOFWEEK(o.order_date) = 2 THEN o.quantity ELSE 0 END) AS Monday,
#        SUM(CASE WHEN DAYOFWEEK(o.order_date) = 3 THEN o.quantity ELSE 0 END) AS Tuesday,
#        SUM(CASE WHEN DAYOFWEEK(o.order_date) = 4 THEN o.quantity ELSE 0 END) AS Wednesday,
#        SUM(CASE WHEN DAYOFWEEK(o.order_date) = 5 THEN o.quantity ELSE 0 END) AS Thursday,
#        SUM(CASE WHEN DAYOFWEEK(o.order_date) = 6 THEN o.quantity ELSE 0 END) AS Friday,
#        SUM(CASE WHEN DAYOFWEEK(o.order_date) = 7 THEN o.quantity ELSE 0 END) AS Saturday,
#        SUM(CASE WHEN DAYOFWEEK(o.order_date) = 1 THEN o.quantity ELSE 0 END) AS Sunday
# FROM Items i
# LEFT JOIN Orders o ON i.item_id = o.item_id
# GROUP BY i.item_category
# ORDER BY i.item_category

class Solution(object):
    pass
