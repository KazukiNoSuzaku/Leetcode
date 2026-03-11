# Given an array of integers nums and an integer k, return the total number of subarrays
# whose sum equals to k.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        count = defaultdict(int)
        count[0] = 1
        prefix = res = 0
        for n in nums:
            prefix += n
            res += count[prefix - k]
            count[prefix] += 1
        return res
