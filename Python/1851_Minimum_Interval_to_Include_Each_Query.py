# Author: Kaustav Ghosh
# Problem: Minimum Interval to Include Each Query
# Approach: Answer queries in increasing order; add intervals once their left end is reached to a min-heap keyed on size, discard intervals that already ended, and the heap top is the smallest covering interval

import heapq

class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        heap = []  # (size, right)
        answer = {}
        i = 0
        n = len(intervals)

        for q in sorted(queries):
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            answer[q] = heap[0][0] if heap else -1

        return [answer[q] for q in queries]
