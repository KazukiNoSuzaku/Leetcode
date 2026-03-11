# Given an integer array nums and an integer k, return true if nums has a good subarray.
# A good subarray is a subarray of length at least 2 whose sum is a multiple of k.

# Author: Kaustav Ghosh

class Solution(object):
    def checkSubarraySum(self, nums, k):
        seen = {0: -1}
        prefix = 0
        for i, n in enumerate(nums):
            prefix = (prefix + n) % k
            if prefix in seen:
                if i - seen[prefix] >= 2:
                    return True
            else:
                seen[prefix] = i
        return False
