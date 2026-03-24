# Author: Kaustav Ghosh
# Problem 2057: Smallest Index With Equal Value

class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1
