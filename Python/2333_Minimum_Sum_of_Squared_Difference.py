# Author: Kaustav Ghosh
# 2333. Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/
# Sort diff array, use heap to reduce largest differences with k1+k2 operations

import heapq

class Solution(object):
    def minSumOfSquaredDifference(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        # Use a max-heap (negate values) to greedily reduce largest differences
        # Sort descending and reduce greedily
        diffs.sort(reverse=True)
        n = len(diffs)

        # Binary search: find max value we can reduce all elements to
        lo, hi = 0, diffs[0]
        while lo < hi:
            mid = (lo + hi) // 2
            # Operations needed to reduce all values to at most mid
            ops = sum(max(0, d - mid) for d in diffs)
            if ops <= k:
                hi = mid
            else:
                lo = mid + 1

        # lo is the minimum possible max diff value
        target = lo
        ops_needed = sum(max(0, d - target) for d in diffs)
        remaining = k - ops_needed

        # Reduce elements equal to target by 1 as much as possible with remaining ops
        result = 0
        for d in diffs:
            val = min(d, target)
            if val == target and remaining > 0:
                val -= 1
                remaining -= 1
            result += val * val

        return result
