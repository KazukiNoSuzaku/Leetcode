# Author: Kaustav Ghosh
# Problem: 2212. Maximum Points in an Archery Competition
# URL: https://leetcode.com/problems/maximum-points-in-an-archery-competition/
# Difficulty: Medium
#
# Approach:
# Use bitmask enumeration over all 2^11 subsets of the 11 scoring sections
# (0..10). For each subset Bob can "win", check if the total arrows needed
# to beat Alice in those sections fits within numArrows. Maximise the score
# points gained. Distribute any leftover arrows into section 0.

class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: list[int]
        :rtype: list[int]
        """
        best_score = 0
        best_mask = 0

        for mask in range(1, 1 << 11):
            score = 0
            arrows_needed = 0
            for i in range(11):
                if mask & (1 << i):
                    score += i
                    arrows_needed += aliceArrows[i] + 1
            if arrows_needed <= numArrows and score > best_score:
                best_score = score
                best_mask = mask

        bob = [0] * 11
        remaining = numArrows
        for i in range(11):
            if best_mask & (1 << i):
                bob[i] = aliceArrows[i] + 1
                remaining -= bob[i]
        # Put leftover arrows in section 0
        bob[0] += remaining
        return bob
