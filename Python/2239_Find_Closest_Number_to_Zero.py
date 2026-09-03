# Author: Kaustav Ghosh
# Problem: Find Closest Number to Zero
# Approach: Pick the element with the smallest absolute value; when two are equally close (e.g. -x and x), prefer the larger one. Sorting by (abs(value), -value) and taking the first captures both rules

class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums, key=lambda x: (abs(x), -x))
