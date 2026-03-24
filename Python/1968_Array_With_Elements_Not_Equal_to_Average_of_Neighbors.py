# Author: Kaustav Ghosh
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = [0] * len(nums)
        idx = 0
        # Place elements in zigzag: even indices get smaller, odd get larger
        for i in range(0, len(nums), 2):
            result[i] = nums[idx]
            idx += 1
        for i in range(1, len(nums), 2):
            result[i] = nums[idx]
            idx += 1
        return result
