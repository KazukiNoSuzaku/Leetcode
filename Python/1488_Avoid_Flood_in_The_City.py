# Author: Kaustav Ghosh
# Problem: Avoid Flood in The City
# Approach: Greedy with sorted set of dry days, assign drying to earliest needed

from sortedcontainers import SortedList

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        import bisect
        n = len(rains)
        result = [-1] * n
        full = {}  # lake -> day it was filled
        dry_days = SortedList()

        for i in range(n):
            if rains[i] == 0:
                dry_days.add(i)
                result[i] = 1  # placeholder, dry any lake
            else:
                lake = rains[i]
                if lake in full:
                    # Need to dry this lake before today
                    prev = full[lake]
                    idx = dry_days.bisect_left(prev)
                    if idx == len(dry_days):
                        return []
                    dry_day = dry_days[idx]
                    result[dry_day] = lake
                    dry_days.remove(dry_day)
                full[lake] = i
        return result
