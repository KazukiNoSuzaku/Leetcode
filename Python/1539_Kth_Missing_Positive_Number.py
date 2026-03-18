# Author: Kaustav Ghosh
# Problem: 1539 - Kth Missing Positive Number
# Approach: Binary search on how many numbers are missing before index

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
            # missing before arr[mid] = arr[mid] - (mid+1)
            if arr[mid] - (mid + 1) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo + k
