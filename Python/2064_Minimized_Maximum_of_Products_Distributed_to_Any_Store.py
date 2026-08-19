# Author: Kaustav Ghosh
# Problem: Minimized Maximum of Products Distributed to Any Store
# Approach: Binary search the maximum products a store may receive. For a candidate x, product type q needs ceil(q/x) stores; the value is feasible if the total stores needed fits within n

class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        def feasible(x):
            return sum((q + x - 1) // x for q in quantities) <= n

        lo, hi = 1, max(quantities)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
