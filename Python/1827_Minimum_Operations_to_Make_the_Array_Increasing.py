# Author: Kaustav Ghosh

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                target = nums[i - 1] + 1
                ops += target - nums[i]
                nums[i] = target
        return ops
