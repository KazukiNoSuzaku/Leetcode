# Author: Kaustav Ghosh
# Problem: 2276. Count Integers in Intervals
# URL: https://leetcode.com/problems/count-integers-in-intervals/
# Difficulty: Hard
#
# Approach:
# Use a sorted list of non-overlapping intervals. On add, find all overlapping
# intervals, merge them into one, and update the total count accordingly.

from bisect import bisect_left, bisect_right, insort

class CountIntervals(object):

    def __init__(self):
        self.intervals = []
        self.cnt = 0

    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        new_left, new_right = left, right
        # Find overlapping intervals
        # An interval [a, b] overlaps [left, right] if a <= right and b >= left
        starts = [iv[0] for iv in self.intervals]
        ends = [iv[1] for iv in self.intervals]

        # Find first interval whose end >= left
        lo = bisect_left(ends, left)
        # Find last interval whose start <= right
        hi = bisect_right(starts, right)

        # Merge all intervals in [lo, hi)
        for i in range(lo, hi):
            new_left = min(new_left, self.intervals[i][0])
            new_right = max(new_right, self.intervals[i][1])
            self.cnt -= self.intervals[i][1] - self.intervals[i][0] + 1

        self.intervals[lo:hi] = [[new_left, new_right]]
        self.cnt += new_right - new_left + 1

    def count(self):
        """
        :rtype: int
        """
        return self.cnt
