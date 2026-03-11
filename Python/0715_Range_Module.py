# Design a Range Module to track ranges of numbers with addRange, queryRange, removeRange.

# Author: Kaustav Ghosh

import bisect

class RangeModule(object):
    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        lo = bisect.bisect_left(self.ranges, left)
        hi = bisect.bisect_right(self.ranges, right)
        if lo % 2 == 0 and hi % 2 == 0:
            self.ranges[lo:hi] = [left, right]
        elif lo % 2 == 0:
            self.ranges[lo:hi] = [left]
        elif hi % 2 == 0:
            self.ranges[lo:hi] = [right]
        else:
            self.ranges[lo:hi] = []

    def queryRange(self, left, right):
        lo = bisect.bisect_right(self.ranges, left)
        hi = bisect.bisect_left(self.ranges, right)
        return lo == hi and lo % 2 == 1

    def removeRange(self, left, right):
        lo = bisect.bisect_left(self.ranges, left)
        hi = bisect.bisect_right(self.ranges, right)
        ins = []
        if lo % 2 == 1: ins.append(left)
        if hi % 2 == 1: ins.append(right)
        self.ranges[lo:hi] = ins
