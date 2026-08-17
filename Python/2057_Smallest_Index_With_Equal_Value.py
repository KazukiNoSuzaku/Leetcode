# Author: Kaustav Ghosh
# Problem: Smallest Index With Equal Value
# Approach: Scan left to right and return the first index i where i mod 10 equals nums[i]

class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, v in enumerate(nums):
            if i % 10 == v:
                return i
        return -1
