# Given an array, count triples (i, j, k) such that nums[i] & nums[j] & nums[k] == 0.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def countTriplets(self, nums):
        pair_count = Counter()
        for a in nums:
            for b in nums:
                pair_count[a & b] += 1
        res = 0
        for c in nums:
            for ab, cnt in pair_count.items():
                if ab & c == 0:
                    res += cnt
        return res
