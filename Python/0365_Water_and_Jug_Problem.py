# You are given two jugs with capacities jug1Capacity and jug2Capacity liters.
# There is an infinite amount of water supply available.
# Determine whether it is possible to measure exactly targetCapacity liters.

# Example 1:
# Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
# Output: true

# Example 2:
# Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
# Output: false

# Constraints:
# 1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6

# Author: Kaustav Ghosh

from math import gcd

class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        total = jug1Capacity + jug2Capacity
        if targetCapacity > total:
            return False
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
