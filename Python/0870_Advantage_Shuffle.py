# Rearrange nums1 to maximize wins against nums2 (each element must beat corresponding).

# Author: Kaustav Ghosh

import heapq
from collections import deque

class Solution(object):
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        indexed = sorted(enumerate(nums2), key=lambda x: -x[1])
        res = [0] * len(nums1)
        lo, hi = 0, len(nums1) - 1
        for i, v in indexed:
            if nums1[hi] > v:
                res[i] = nums1[hi]; hi -= 1
            else:
                res[i] = nums1[lo]; lo += 1
        return res
