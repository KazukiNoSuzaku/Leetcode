# You are given an array of intervals, where intervals[i] = [starti, endi].
# For each interval i, return the index j such that intervals[j].start >= intervals[i].end
# and intervals[j].start is minimized. Return -1 if no such j exists.

# Author: Kaustav Ghosh

import bisect

class Solution(object):
    def findRightInterval(self, intervals):
        start_sorted = sorted((s, i) for i, (s, e) in enumerate(intervals))
        starts = [s for s, _ in start_sorted]
        res = []
        for s, e in intervals:
            idx = bisect.bisect_left(starts, e)
            res.append(start_sorted[idx][1] if idx < len(starts) else -1)
        return res
