# Author: Kaustav Ghosh
# Problem: Sum of Absolute Differences in a Sorted Array
# Approach: Since sorted, elements left of i are all smaller and right are all larger; use running left-sum and total to get each answer in O(1)

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total = sum(nums)
        res = [0] * n
        left = 0
        for i in range(n):
            right = total - left - nums[i]
            res[i] = (nums[i] * i - left) + (right - nums[i] * (n - 1 - i))
            left += nums[i]
        return res
