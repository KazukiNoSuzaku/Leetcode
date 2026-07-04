# Author: Kaustav Ghosh
# Problem: Special Array With X Elements Greater Than or Equal X
# Approach: Sort, then for each candidate x count elements >= x with binary search; the unique x where that count equals x is the answer

from bisect import bisect_left

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        for x in range(1, n + 1):
            ge = n - bisect_left(nums, x)
            if ge == x:
                return x
        return -1
