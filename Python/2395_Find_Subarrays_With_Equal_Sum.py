# Author: Kaustav Ghosh
# Problem: Find Subarrays With Equal Sum
# Approach: The subarrays have length 2, so collect the sums of adjacent pairs in a set and report as soon as one repeats

class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for a, b in zip(nums, nums[1:]):
            if a + b in seen:
                return True
            seen.add(a + b)
        return False
