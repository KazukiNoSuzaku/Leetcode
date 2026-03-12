# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Binary search on minimum chunk sweetness

class Solution(object):
    def maximizeSweetness(self, sweetness, k):
        """
        :type sweetness: List[int]
        :type k: int
        :rtype: int
        """
        lo, hi = min(sweetness), sum(sweetness) // (k + 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            chunks = 0
            cur = 0
            for s in sweetness:
                cur += s
                if cur >= mid:
                    chunks += 1
                    cur = 0
            if chunks >= k + 1:
                lo = mid
            else:
                hi = mid - 1
        return lo
