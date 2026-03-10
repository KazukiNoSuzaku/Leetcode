# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers
# seen so far as a list of disjoint intervals.
# Implement the SummaryRanges class:
# - SummaryRanges() initializes the object with an empty stream.
# - void addNum(int value) adds the integer value to the stream.
# - int[][] getIntervals() returns a summary of the integers in the stream currently as a list
#   of disjoint intervals [starti, endi].

# Example 1:
# Input: ["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]
#        [[],[1],[],[3],[],[7],[],[2],[],[6],[]]
# Output: [null,null,[[1,1]],null,[[1,1],[3,3]],null,[[1,1],[3,3],[7,7]],null,[[1,3],[7,7]],null,[[1,3],[6,7]]]

# Constraints:
# 0 <= value <= 10^4
# At most 3 * 10^4 calls will be made to addNum and getIntervals.

# Author: Kaustav Ghosh

import bisect

class SummaryRanges(object):
    def __init__(self):
        self.intervals = []

    def addNum(self, value):
        new = [value, value]
        left = bisect.bisect_right(self.intervals, [value]) - 1
        right = bisect.bisect_left(self.intervals, [value + 1])
        merge_left = left >= 0 and self.intervals[left][1] >= value - 1
        merge_right = right < len(self.intervals) and self.intervals[right][0] <= value + 1
        if merge_left and merge_right:
            self.intervals[left][1] = max(self.intervals[left][1], self.intervals[right][1])
            del self.intervals[right]
        elif merge_left:
            self.intervals[left][1] = max(self.intervals[left][1], value)
        elif merge_right:
            self.intervals[right][0] = min(self.intervals[right][0], value)
        else:
            self.intervals.insert(right, new)

    def getIntervals(self):
        return self.intervals
