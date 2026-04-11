# Author: Kaustav Ghosh
# Problem: 2270. Number of Ways to Split Array
# URL: https://leetcode.com/problems/number-of-ways-to-split-array/
# Difficulty: Medium
#
# Approach:
# Compute total sum. Iterate with prefix sum; at each split point check
# if left sum >= right sum (total - left).

class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        count = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum >= total - left_sum:
                count += 1
        return count
