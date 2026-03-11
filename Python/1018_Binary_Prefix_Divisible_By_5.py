# For each prefix of binary array nums, return whether its value is divisible by 5.

# Author: Kaustav Ghosh

class Solution(object):
    def prefixesDivBy5(self, nums):
        val = 0
        res = []
        for b in nums:
            val = (val * 2 + b) % 5
            res.append(val == 0)
        return res
