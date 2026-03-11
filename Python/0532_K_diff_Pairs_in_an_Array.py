# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
# A k-diff pair is an integer pair (nums[i], nums[j]) where |nums[i] - nums[j]| == k.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        if k < 0: return 0
        count = Counter(nums)
        res = 0
        for n in count:
            if k == 0:
                if count[n] > 1: res += 1
            else:
                if n + k in count: res += 1
        return res
