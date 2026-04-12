# Author: Kaustav Ghosh
# Problem: 2295. Replace Elements in an Array
# URL: https://leetcode.com/problems/replace-elements-in-an-array/
# Difficulty: Medium

class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        val_to_idx = {}
        for i, v in enumerate(nums):
            val_to_idx[v] = i
        for old, new in operations:
            idx = val_to_idx[old]
            nums[idx] = new
            del val_to_idx[old]
            val_to_idx[new] = idx
        return nums
