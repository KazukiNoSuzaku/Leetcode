# Author: Kaustav Ghosh
# Problem 2054: Two Best Non-Overlapping Events

from bisect import bisect_right

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        n = len(events)
        # suffix_max[i] = max value from events[i:]
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        starts = [e[0] for e in events]
        ans = 0
        for start, end, val in events:
            # Find first event starting after this one ends
            idx = bisect_right(starts, end)
            best_second = suffix_max[idx] if idx < n else 0
            ans = max(ans, val + best_second)
        return ans
