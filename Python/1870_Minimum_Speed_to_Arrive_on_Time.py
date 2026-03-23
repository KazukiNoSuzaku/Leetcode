# Author: Kaustav Ghosh
# Problem 1870: Minimum Speed to Arrive on Time

import math

class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        if len(dist) - 1 >= hour:
            return -1

        def can_arrive(speed):
            total = 0.0
            for i in range(len(dist) - 1):
                total += math.ceil(dist[i] / float(speed))
            total += dist[-1] / float(speed)
            return total <= hour

        lo, hi = 1, 10 ** 7
        while lo < hi:
            mid = (lo + hi) // 2
            if can_arrive(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
