# Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
# where 0 <= i <= j < n.

# Author: Kaustav Ghosh

class Solution(object):
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefixes = {n & mask for n in nums}
            candidate = max_xor | (1 << i)
            if any(candidate ^ p in prefixes for p in prefixes):
                max_xor = candidate
        return max_xor
