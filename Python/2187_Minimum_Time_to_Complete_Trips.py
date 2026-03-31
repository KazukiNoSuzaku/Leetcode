# Author: Kaustav Ghosh
# 2187. Minimum Time to Complete Trips
# https://leetcode.com/problems/minimum-time-to-complete-trips/
# Difficulty: Medium
#
# Approach: Binary search on time t. For a given time t, bus i completes
# t // time[i] trips. Check if the total trips >= totalTrips.
# Search range: [1, min(time) * totalTrips].
# Time: O(n * log(min_time * totalTrips)), Space: O(1)

class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        def can_complete(t):
            return sum(t // ti for ti in time) >= totalTrips

        lo, hi = 1, min(time) * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            if can_complete(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
