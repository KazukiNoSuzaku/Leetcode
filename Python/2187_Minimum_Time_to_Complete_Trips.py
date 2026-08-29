# Author: Kaustav Ghosh
# Problem: Minimum Time to Complete Trips
# Approach: In time t a bus with per-trip time p completes t // p trips, so total trips is a monotonically non-decreasing function of t. Binary search for the smallest t whose total trips reaches totalTrips

class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        lo, hi = 1, min(time) * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            trips = sum(mid // p for p in time)
            if trips >= totalTrips:
                hi = mid
            else:
                lo = mid + 1
        return lo
