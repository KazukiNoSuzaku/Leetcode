# Author: Kaustav Ghosh
# Problem 2064: Minimized Maximum of Products Distributed to Any Store

class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        def can_distribute(max_per_store):
            stores_needed = 0
            for q in quantities:
                stores_needed += (q + max_per_store - 1) // max_per_store
            return stores_needed <= n

        lo, hi = 1, max(quantities)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_distribute(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
