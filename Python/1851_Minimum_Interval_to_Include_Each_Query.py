# Author: Kaustav Ghosh
# Problem 1851: Minimum Interval to Include Each Query

import heapq

class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        result = [-1] * len(queries)
        heap = []
        i = 0
        for qi, q in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                result[qi] = heap[0][0]
        return result
