# Author: Kaustav Ghosh
# Problem: 2294. Partition Array Such That Maximum Difference Is K
# URL: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
# Difficulty: Medium

class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        groups = 1
        group_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - group_min > k:
                groups += 1
                group_min = nums[i]
        return groups
