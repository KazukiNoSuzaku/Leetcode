# Author: Kaustav Ghosh
# Problem: 2162. Minimum Cost to Set Cooking Time
# URL: https://leetcode.com/problems/minimum-cost-to-set-cooking-time/
# Difficulty: Medium
# Note: Premium problem

# SQL/Python approach:
# Enumerate all valid (minute, second) representations of targetSeconds.
# For each valid (m, s) pair (0 <= m <= 99, 0 <= s <= 99, m*60+s == targetSeconds
# or falls within range), simulate the cost of moving from startAt to each digit.
# Cost to press a digit = abs(current - digit) * moveCost + pushCost.
# Return the minimum cost across all valid representations.

class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        def cost(m, s):
            if not (0 <= m <= 99 and 0 <= s <= 99):
                return float('inf')
            digits = str(m * 100 + s)
            cur = startAt
            total = 0
            for d in digits:
                d = int(d)
                if d != cur:
                    total += moveCost
                    cur = d
                total += pushCost
            return total

        m1, s1 = targetSeconds // 60, targetSeconds % 60
        return min(cost(m1, s1), cost(m1 - 1, s1 + 60))
