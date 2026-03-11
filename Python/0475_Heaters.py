# Winter is coming! During the contest, your target is to design a standard heater with
# a fixed warm radius so that all the houses can be covered by your heaters.
# Return the minimum radius standard heaters need so that those heaters could cover all houses.

# Author: Kaustav Ghosh

import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        res = 0
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            dist = float('inf')
            if idx < len(heaters):
                dist = min(dist, heaters[idx] - house)
            if idx > 0:
                dist = min(dist, house - heaters[idx - 1])
            res = max(res, dist)
        return res
