# Find minimum eating speed k to finish all piles within h hours.

# Author: Kaustav Ghosh

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(math.ceil(p / float(mid)) for p in piles) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo
