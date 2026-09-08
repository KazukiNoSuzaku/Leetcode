# Author: Kaustav Ghosh
# Problem: Count Integers in Intervals
# Approach: Keep the added ranges as a set of disjoint intervals sorted by start (with parallel start/end lists) plus a running count of covered integers. On add, the intervals overlapping [left, right] form a contiguous block (found by binary search on ends and starts); remove them, subtract their lengths, merge into one interval spanning the union, and add its length back

import bisect


class CountIntervals(object):
    def __init__(self):
        self.starts = []
        self.ends = []
        self.total = 0

    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        # first overlapping interval: end >= left
        lo = bisect.bisect_left(self.ends, left)
        # last overlapping interval: start <= right
        hi = bisect.bisect_right(self.starts, right) - 1

        new_l, new_r = left, right
        if lo <= hi:
            new_l = min(new_l, self.starts[lo])
            new_r = max(new_r, self.ends[hi])
            # remove merged block, subtracting their covered lengths
            for i in range(lo, hi + 1):
                self.total -= self.ends[i] - self.starts[i] + 1
            del self.starts[lo:hi + 1]
            del self.ends[lo:hi + 1]

        self.starts.insert(lo, new_l)
        self.ends.insert(lo, new_r)
        self.total += new_r - new_l + 1

    def count(self):
        """
        :rtype: int
        """
        return self.total
