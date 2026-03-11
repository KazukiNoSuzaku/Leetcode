# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        ab_sum = defaultdict(int)
        for a in nums1:
            for b in nums2:
                ab_sum[a + b] += 1
        res = 0
        for c in nums3:
            for d in nums4:
                res += ab_sum[-(c + d)]
        return res
