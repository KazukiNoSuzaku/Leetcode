# Author: Kaustav Ghosh
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total = sum(nums)
        prefix = 0
        result = []
        for i in range(n):
            left_sum = prefix
            right_sum = total - prefix - nums[i]
            val = nums[i] * i - left_sum + right_sum - nums[i] * (n - i - 1)
            result.append(val)
            prefix += nums[i]
        return result
