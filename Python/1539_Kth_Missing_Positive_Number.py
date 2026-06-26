# Author: Kaustav Ghosh
# Problem: Kth Missing Positive Number
# Approach: Binary search on arr — at index i, arr[i]-(i+1) numbers are missing before arr[i]; find leftmost index where missing >= k

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo + k
