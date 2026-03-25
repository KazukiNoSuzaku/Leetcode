# Author: Kaustav Ghosh
# Problem 2091: Removing Minimum and Maximum From Array

class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)
        # Option 1: Remove both from the left
        opt1 = right + 1
        # Option 2: Remove both from the right
        opt2 = n - left
        # Option 3: Remove left one from left, right one from right
        opt3 = (left + 1) + (n - right)
        return min(opt1, opt2, opt3)
