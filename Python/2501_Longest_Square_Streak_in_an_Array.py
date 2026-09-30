# Author: Kaustav Ghosh
# Problem: Longest Square Streak in an Array
# Approach: Order does not matter for a subsequence that can be reordered, so put the values in a set and, from each one, keep squaring while the result is present. Values are at least 2, so each chain grows past the limit within a handful of steps

class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        present = set(nums)
        best = -1
        for start in present:
            length = 0
            value = start
            while value in present:
                length += 1
                value *= value
            if length >= 2:
                best = max(best, length)
        return best
