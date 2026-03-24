# Author: Kaustav Ghosh
# Problem 2016: Maximum Difference Between Increasing Elements

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        result = -1
        for i in range(1, len(nums)):
            if nums[i] > min_val:
                result = max(result, nums[i] - min_val)
            min_val = min(min_val, nums[i])
        return result
