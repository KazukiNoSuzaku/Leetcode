# Author: Kaustav Ghosh
# Problem: Pour Water Between Buckets to Make Water Levels Equal
# Approach: Binary search the final equal level. For a candidate level, buckets above it supply surplus (reduced by the pour loss) and buckets below need the deficit. The level is achievable when the delivered surplus covers the deficit; find the largest such level

class Solution(object):
    def equalizeWater(self, buckets, loss):
        """
        :type buckets: List[int]
        :type loss: int
        :rtype: float
        """
        keep = (100 - loss) / 100.0

        def feasible(level):
            surplus = sum(b - level for b in buckets if b > level)
            deficit = sum(level - b for b in buckets if b < level)
            return surplus * keep >= deficit

        lo, hi = 0.0, float(max(buckets))
        for _ in range(100):
            mid = (lo + hi) / 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid
        return lo
