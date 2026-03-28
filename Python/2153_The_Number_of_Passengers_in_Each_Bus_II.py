# Author: Kaustav Ghosh
# Problem: 2153. The Number of Passengers in Each Bus II
# URL: https://leetcode.com/problems/the-number-of-passengers-in-each-bus-ii/
# Premium SQL Problem
#
# SQL Approach:
# For each bus, find all passengers whose arrival time is within the range
# (previous bus arrival, current bus arrival]. Then for each bus, compute
# how many passengers actually board given capacity constraints, carrying
# over unboarded passengers to the next bus using cumulative sums.
#
# WITH ranked_buses AS (
#     SELECT bus_id, arrival_time, capacity,
#            LAG(arrival_time, 1, 0) OVER (ORDER BY arrival_time) AS prev_arrival
#     FROM Buses
# ),
# passenger_counts AS (
#     SELECT b.bus_id, b.arrival_time, b.capacity, b.prev_arrival,
#            COUNT(p.passenger_id) AS waiting
#     FROM ranked_buses b
#     LEFT JOIN Passengers p
#     ON p.arrival_time > b.prev_arrival AND p.arrival_time <= b.arrival_time
#     GROUP BY b.bus_id, b.arrival_time, b.capacity, b.prev_arrival
# )
# -- Then carry forward overflow using cumulative capacity logic

class Solution(object):
    pass
