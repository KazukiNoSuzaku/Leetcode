# Find the k-th smallest number in an m x n multiplication table.

# Author: Kaustav Ghosh

class Solution(object):
    def findKthNumber(self, m, n, k):
        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            count = sum(min(mid // i, n) for i in range(1, m + 1))
            if count >= k: hi = mid
            else: lo = mid + 1
        return lo
