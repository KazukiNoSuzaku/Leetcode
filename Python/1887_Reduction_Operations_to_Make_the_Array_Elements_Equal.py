# Author: Kaustav Ghosh
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ops = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count += 1
            ops += count
        return ops
