# Author: Kaustav Ghosh
# Problem 1834: Single-Threaded CPU

import heapq

class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        indexed = sorted(enumerate(tasks), key=lambda x: x[1][0])
        result = []
        heap = []
        time = 0
        i = 0
        n = len(indexed)
        while i < n or heap:
            if not heap and i < n and indexed[i][1][0] > time:
                time = indexed[i][1][0]
            while i < n and indexed[i][1][0] <= time:
                idx, (enqueue, proc) = indexed[i]
                heapq.heappush(heap, (proc, idx))
                i += 1
            proc_time, idx = heapq.heappop(heap)
            time += proc_time
            result.append(idx)
        return result
