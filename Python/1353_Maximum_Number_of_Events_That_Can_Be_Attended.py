# Author: Kaustav Ghosh
# Problem: Maximum Number of Events That Can Be Attended
# Approach: Greedy with min-heap by end day

import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        heap = []
        i, n = 0, len(events)
        count = 0
        day = 1
        while i < n or heap:
            if not heap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                count += 1
            day += 1
        return count
