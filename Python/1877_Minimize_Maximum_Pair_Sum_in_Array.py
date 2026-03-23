# Author: Kaustav Ghosh
# Problem 1877: Minimize Maximum Pair Sum in Array

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        n = len(nums)
        for i in range(n // 2):
            result = max(result, nums[i] + nums[n - 1 - i])
        return result
