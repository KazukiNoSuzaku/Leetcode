# Author: Kaustav Ghosh
# Problem: 2238. Number of Times a Driver Was a Passenger
# URL: https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/
# Difficulty: Medium
# Note: Premium SQL problem
#
# SQL Approach:
# Get all distinct drivers from the driver_id column, then LEFT JOIN with
# the passenger_id column to count how many times each driver appeared as
# a passenger.
#
# SELECT d.driver_id,
#        COUNT(t2.passenger_id) AS cnt
# FROM (SELECT DISTINCT driver_id FROM Rides) d
# LEFT JOIN Rides t2
#     ON d.driver_id = t2.passenger_id
# GROUP BY d.driver_id;

class Solution(object):
    pass
