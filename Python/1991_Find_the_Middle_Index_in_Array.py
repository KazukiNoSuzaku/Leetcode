# Author: Kaustav Ghosh
# Problem: Find the Middle Index in Array
# Approach: Scan left to right tracking the running left sum. At each index the right sum is total - left - nums[i]; return the first index where they match

class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0
        for i, v in enumerate(nums):
            if left == total - left - v:
                return i
            left += v
        return -1
