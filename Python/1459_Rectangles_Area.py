# Author: Kaustav Ghosh
# Problem: Rectangles Area (Premium SQL)
# Approach: Self-join Points table to form rectangles, compute area
#
# SQL Solution:
# SELECT p1.id AS p1, p2.id AS p2,
#        ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) AS area
# FROM Points p1
# JOIN Points p2 ON p1.id < p2.id
# WHERE p1.x_value != p2.x_value AND p1.y_value != p2.y_value
# ORDER BY area DESC, p1, p2

class Solution(object):
    pass
