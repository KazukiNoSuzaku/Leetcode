# Author: Kaustav Ghosh
# Problem 2040: Kth Smallest Product of Two Sorted Arrays

from bisect import bisect_right, bisect_left

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        def count_le(val):
            """Count pairs with product <= val."""
            cnt = 0
            for a in nums1:
                if a > 0:
                    # a * b <= val => b <= val / a
                    target = val / float(a)
                    cnt += bisect_right(nums2, target)
                elif a < 0:
                    # a * b <= val => b >= val / a (inequality flips)
                    target = val / float(a)
                    cnt += len(nums2) - bisect_left(nums2, target)
                    # Need b >= ceil(val/a) for integers
                    # Actually need a*b <= val
                    # Recount precisely for integers
                else:
                    # a == 0, product is 0
                    if val >= 0:
                        cnt += len(nums2)
            return cnt

        def count_le_precise(val):
            """Count pairs with product <= val using integer math."""
            cnt = 0
            for a in nums1:
                if a > 0:
                    if val >= 0:
                        q = val // a
                        cnt += bisect_right(nums2, q)
                    else:
                        # val < 0, a > 0: b <= val/a < 0
                        # val // a rounds toward negative infinity in Python 2
                        q = -((-val + a - 1) // a)
                        cnt += bisect_right(nums2, q)
                elif a < 0:
                    if val >= 0:
                        # a*b <= val, a < 0 => b >= val/a
                        q = -(val // (-a))
                        cnt += len(nums2) - bisect_left(nums2, q)
                    else:
                        # val < 0, a < 0 => b >= val/a > 0
                        q = (-val) // (-a)
                        if (-val) % (-a) != 0:
                            q += 1
                        cnt += len(nums2) - bisect_left(nums2, q)
                else:
                    if val >= 0:
                        cnt += len(nums2)
            return cnt

        lo, hi = -10**10, 10**10
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count_le_precise(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
