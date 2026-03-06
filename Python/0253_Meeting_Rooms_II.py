# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of conference rooms required.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1

# Constraints:
# 1 <= intervals.length <= 10^4
# 0 <= starti < endi <= 10^6

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)
