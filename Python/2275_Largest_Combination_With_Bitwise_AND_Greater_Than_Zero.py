# Author: Kaustav Ghosh
# Problem: 2275. Largest Combination With Bitwise AND Greater Than Zero
# URL: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
# Difficulty: Medium
#
# Approach:
# For each bit position, count how many candidates have that bit set.
# The answer is the maximum count across all bit positions.

class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        best = 0
        for bit in range(24):
            count = 0
            for num in candidates:
                if num & (1 << bit):
                    count += 1
            best = max(best, count)
        return best
