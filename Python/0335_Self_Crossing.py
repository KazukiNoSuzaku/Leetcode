# You are given an array of integers distance.
# You start at the point (0, 0), and you move distance[0] meters to the north, then
# distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east,
# and so on. In other words, after each move, your direction changes counter-clockwise.
# Return true if your path crosses itself or false if it does not.

# Example 1:
# Input: distance = [2,1,1,2]
# Output: true

# Example 2:
# Input: distance = [1,2,3,4]
# Output: false

# Constraints:
# 1 <= distance.length <= 10^5
# 1 <= distance[i] <= 10^5

# Author: Kaustav Ghosh

class Solution(object):
    def isSelfCrossing(self, distance):
        d = distance
        for i in range(3, len(d)):
            # Case 1: current line crosses the line 3 steps ahead
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True
            # Case 2: current line crosses the line 4 steps ahead
            if i >= 4 and d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                return True
            # Case 3: current line crosses the line 5 steps ahead
            if i >= 5 and d[i-2] >= d[i-4] and d[i] + d[i-4] >= d[i-2] and d[i-1] <= d[i-3] and d[i-1] + d[i-5] >= d[i-3]:
                return True
        return False
