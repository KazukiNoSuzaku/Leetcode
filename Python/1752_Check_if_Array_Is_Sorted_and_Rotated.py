# Author: Kaustav Ghosh
# Problem: Check if Array Is Sorted and Rotated
# Approach: A rotated sorted array wraps around at most once, so count the cyclic positions where the value drops; at most one such drop is allowed

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        drops = sum(1 for i in range(n) if nums[i] > nums[(i + 1) % n])
        return drops <= 1
