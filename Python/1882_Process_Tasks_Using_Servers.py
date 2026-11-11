# Author: Kaustav Ghosh
# Problem: Process Tasks Using Servers
# Approach: Two heaps split the servers by state: the free ones ordered by weight then index, which is exactly the selection rule, and the busy ones ordered by the moment they come back. At each second the busy servers whose time has arrived are returned to the free heap, and if nothing is free the clock jumps straight to the next release instead of ticking, since nothing can happen in between. A task that waits does not lose its place, because tasks are taken strictly in order and the clock never moves backwards; each server therefore changes heap once per task it runs.

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        from heapq import heapify, heappop, heappush

        free = [(weight, index) for index, weight in enumerate(servers)]
        heapify(free)
        busy = []

        answer = []
        clock = 0
        for task, duration in enumerate(tasks):
            if clock < task:
                clock = task
            if not free:
                clock = max(clock, busy[0][0])
            while busy and busy[0][0] <= clock:
                _, weight, index = heappop(busy)
                heappush(free, (weight, index))
            weight, index = heappop(free)
            heappush(busy, (clock + duration, weight, index))
            answer.append(index)
        return answer
