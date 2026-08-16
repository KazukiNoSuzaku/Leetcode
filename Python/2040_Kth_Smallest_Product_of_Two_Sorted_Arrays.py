# Author: Kaustav Ghosh
# Problem: Kth Smallest Product of Two Sorted Arrays
# Approach: Binary search the product value. For a candidate mid, count products <= mid: for each a in nums1 the valid b form a prefix or suffix of the sorted nums2 depending on a's sign, found with integer floor/ceil thresholds. The smallest value whose count reaches k is the answer

import bisect

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        n2 = len(nums2)

        def count_leq(mid):
            total = 0
            for a in nums1:
                if a > 0:
                    # b <= floor(mid / a)
                    total += bisect.bisect_right(nums2, mid // a)
                elif a < 0:
                    # b >= ceil(mid / a) = -(mid // (-a))
                    thr = -(mid // (-a))
                    total += n2 - bisect.bisect_left(nums2, thr)
                else:
                    if mid >= 0:
                        total += n2
            return total

        lo, hi = -10 ** 10, 10 ** 10
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
