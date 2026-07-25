# Author: Kaustav Ghosh
# Problem: Single-Threaded CPU
# Approach: Sort tasks by enqueue time; advance a clock, pushing all available tasks into a min-heap keyed on (processing time, index), and always run the smallest. Jump the clock forward when idle

import heapq

class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        indexed = sorted(range(len(tasks)), key=lambda i: tasks[i][0])
        order = []
        available = []  # (processing_time, index)
        time = 0
        i = 0
        n = len(tasks)

        while len(order) < n:
            while i < n and tasks[indexed[i]][0] <= time:
                idx = indexed[i]
                heapq.heappush(available, (tasks[idx][1], idx))
                i += 1
            if not available:
                time = tasks[indexed[i]][0]  # idle: jump to next enqueue
                continue
            proc, idx = heapq.heappop(available)
            time += proc
            order.append(idx)
        return order
