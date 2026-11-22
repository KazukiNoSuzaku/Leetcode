# Author: Kaustav Ghosh
# Problem: Find the Middle Index in Array
# Approach: The middle index splits the array so the numbers before it sum to the same value as the numbers after it, so one running prefix sum is enough. Keep the total of the whole array, then walk left to right carrying the sum of everything strictly before the current index; the suffix after the index is the total minus the prefix minus the current element, and the first index where those two agree is the answer. A single pass after the total is computed, and -1 if no index works.

class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        prefix = 0
        for index, value in enumerate(nums):
            if prefix == total - prefix - value:
                return index
            prefix += value
        return -1
