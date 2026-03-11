# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest non-overlapping.

# Author: Kaustav Ghosh

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                count += 1
        return count
