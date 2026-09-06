# Author: Kaustav Ghosh
# Problem: Number of Ways to Split Array
# Approach: A split at index i is valid when the sum of the first i+1 elements is at least the sum of the rest. Track the running left sum; the right sum is the total minus the left. Count valid split points i from 0 to n-2

class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0
        count = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= total - left:
                count += 1
        return count
