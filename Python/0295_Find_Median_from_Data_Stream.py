# The median is the middle value in an ordered integer list. If the size of the list is even,
# there is no middle value, and the median is the mean of the two middle values.
# Implement the MedianFinder class:
# - MedianFinder() initializes the MedianFinder object.
# - void addNum(int num) adds the integer num from the data stream to the data structure.
# - double findMedian() returns the median of all elements so far.

# Example 1:
# Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
#        [[], [1], [2], [], [3], []]
# Output: [null, null, null, 1.5, null, 2.0]

# Constraints:
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.

# Author: Kaustav Ghosh

import heapq

class MedianFinder(object):
    def __init__(self):
        self.lo = []  # max-heap (invert values)
        self.hi = []  # min-heap

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0
