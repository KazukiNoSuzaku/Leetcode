# Author: Kaustav Ghosh
# Problem: Single-Threaded CPU
# Approach: The processor only ever chooses among the tasks that have already arrived, so the tasks are visited in order of arrival and moved into a heap keyed by processing time with the index as the tie-break, which is exactly the rule for picking the next one. After each task finishes the clock advances by its duration, and every task that arrived during that stretch joins the heap before the next choice. When the heap empties the clock jumps forward to the next arrival rather than ticking, which keeps the work proportional to the number of tasks even though arrival times reach a billion.

class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        from heapq import heappop, heappush

        n = len(tasks)
        arrival = sorted(range(n), key=lambda i: tasks[i][0])
        waiting = []
        order = []
        clock = 0
        nxt = 0
        while len(order) < n:
            if not waiting and clock < tasks[arrival[nxt]][0]:
                clock = tasks[arrival[nxt]][0]
            while nxt < n and tasks[arrival[nxt]][0] <= clock:
                index = arrival[nxt]
                heappush(waiting, (tasks[index][1], index))
                nxt += 1
            duration, index = heappop(waiting)
            clock += duration
            order.append(index)
        return order
