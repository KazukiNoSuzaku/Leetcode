# Author: Kaustav Ghosh
# https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/

# Premium SQL Problem
# SELECT b.bus_id,
#        COUNT(p.passenger_id) AS passengers_cnt
# FROM Buses b
# LEFT JOIN Passengers p
#   ON p.arrival_time <= b.arrival_time
# LEFT JOIN Buses b2
#   ON b2.arrival_time < b.arrival_time
#      AND p.arrival_time <= b2.arrival_time
# WHERE b2.bus_id IS NULL
# GROUP BY b.bus_id
# ORDER BY b.bus_id;

class Solution(object):
    pass
