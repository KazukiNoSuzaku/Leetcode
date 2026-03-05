# There are n gas stations along a circular route, where the amount of gas at the ith station
# is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
# from the ith station to its next (i + 1)th station.
# If you can travel around the circuit once in the clockwise direction, return the starting
# gas station's index, otherwise return -1.

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3

# Example 2:
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1

# Constraints:
# n == gas.length == cost.length
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start
