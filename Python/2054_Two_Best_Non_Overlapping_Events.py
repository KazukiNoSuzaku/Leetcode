# Author: Kaustav Ghosh
# Problem: Two Best Non-Overlapping Events
# Approach: Sort events by start and precompute a suffix maximum of values. For each event, binary search the first event starting strictly after this one ends and combine with the best value from there. Track the best single or pair

import bisect

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        n = len(events)
        starts = [e[0] for e in events]
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        best = 0
        for start, end, value in events:
            j = bisect.bisect_right(starts, end)
            best = max(best, value + suffix_max[j])
        return best
