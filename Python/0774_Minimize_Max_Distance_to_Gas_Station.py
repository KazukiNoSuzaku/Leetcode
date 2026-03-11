# Add k gas stations to minimize max distance between any two adjacent stations.

# Author: Kaustav Ghosh

class Solution(object):
    def minmaxGasDist(self, stations, k):
        lo, hi = 0, stations[-1] - stations[0]
        def count_needed(d):
            return sum(int((stations[i+1]-stations[i])/d) for i in range(len(stations)-1))
        for _ in range(100):
            mid = (lo + hi) / 2.0
            if count_needed(mid) <= k: hi = mid
            else: lo = mid
        return lo
