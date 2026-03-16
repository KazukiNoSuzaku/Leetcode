# Author: Kaustav Ghosh
# Problem: Minimum Number of Days to Make m Bouquets
# Approach: Binary search on days, check feasibility

class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1

        def feasible(days):
            bouquets = 0
            flowers = 0
            for b in bloomDay:
                if b <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
