# Author: Kaustav Ghosh
# Problem: Minimum Speed to Arrive on Time
# Approach: Total time decreases monotonically with speed, so binary search it. All legs but the last round their time up to the next hour (integer waits); the last leg is exact

from math import ceil

class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        n = len(dist)
        if hour <= n - 1:  # even instantaneous last leg cannot help
            return -1

        def travel_time(speed):
            total = 0
            for d in dist[:-1]:
                total += -(-d // speed)  # ceil division
            total += dist[-1] / float(speed)
            return total

        lo, hi = 1, 10 ** 7
        while lo < hi:
            mid = (lo + hi) // 2
            if travel_time(mid) <= hour:
                hi = mid
            else:
                lo = mid + 1
        return lo
