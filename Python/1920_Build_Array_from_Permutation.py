# Author: Kaustav Ghosh
# Problem: Build Array from Permutation
# Approach: Directly build ans[i] = nums[nums[i]] for every index

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[nums[i]] for i in range(len(nums))]
