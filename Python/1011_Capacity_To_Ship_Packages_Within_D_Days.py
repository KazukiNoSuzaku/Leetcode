# Find minimum ship capacity to ship all packages within D days.

# Author: Kaustav Ghosh

class Solution(object):
    def shipWithinDays(self, weights, days):
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            need = cur = 1
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo
