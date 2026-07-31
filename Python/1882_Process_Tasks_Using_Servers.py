# Author: Kaustav Ghosh
# Problem: Process Tasks Using Servers
# Approach: A free min-heap keyed on (weight, index) and a busy min-heap keyed on free time. Advance the clock (jumping forward when no server is free), release finished servers, then assign the front task to the best free server

import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  # (free_time, weight, index)
        answer = []

        time = 0
        for t, duration in enumerate(tasks):
            time = max(time, t)
            # if nothing is free, jump to when the next server frees up
            if not free:
                time = max(time, busy[0][0])
            while busy and busy[0][0] <= time:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            answer.append(i)
            heapq.heappush(busy, (time + duration, w, i))

        return answer
