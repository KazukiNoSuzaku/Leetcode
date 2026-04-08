# Author: Kaustav Ghosh
# Problem: 2240. Number of Ways to Buy Pens and Pencils
# URL: https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/
# Difficulty: Medium
#
# Approach:
# For each possible number of pens (0 to total // cost1), compute the
# remaining budget and count how many pencils can be bought (0 to
# remaining // cost2), which gives remaining // cost2 + 1 ways.

class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        ways = 0
        pens = 0
        while pens * cost1 <= total:
            remaining = total - pens * cost1
            ways += remaining // cost2 + 1
            pens += 1
        return ways
