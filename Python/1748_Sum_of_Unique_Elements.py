# Author: Kaustav Ghosh
# Problem: Sum of Unique Elements
# Approach: An element counts only if it occurs exactly once, which is a property of the whole array rather than of any position, so the counts are tallied in one pass and then the values whose tally is one are added. Two passes over short data is clearer than trying to decide uniqueness while still reading.

from collections import Counter


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = Counter(nums)
        return sum(value for value, count in times.items() if count == 1)
