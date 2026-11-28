# Author: Kaustav Ghosh
# Problem: Second Minimum Time to Reach Destination
# Approach: Every edge costs the same, and the waiting imposed by the signals depends only on how many edges have already been crossed, so a journey's total time is determined entirely by its number of edges and longer journeys always take longer. That reduces the problem to finding the second smallest number of edges on any walk to the destination, which a breadth-first search supplies by recording up to two distinct step counts per vertex and only enqueueing a vertex when it has found a genuinely new one. Such a count always exists, since stepping onto a neighbour and back adds two edges to any walk. The time is then replayed step by step: before each departure the clock is pushed forward to the next green interval if the signal is currently red, and the edge cost is added.

class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        from collections import deque
        neighbours = [[] for _ in range(n + 1)]
        for first, second in edges:
            neighbours[first].append(second)
            neighbours[second].append(first)

        INFINITE = float('inf')
        shortest = [INFINITE] * (n + 1)
        runner_up = [INFINITE] * (n + 1)
        shortest[1] = 0
        queue = deque([(1, 0)])
        while queue:
            node, steps = queue.popleft()
            ahead = steps + 1
            for following in neighbours[node]:
                if ahead < shortest[following]:
                    shortest[following] = ahead
                    queue.append((following, ahead))
                elif shortest[following] < ahead < runner_up[following]:
                    runner_up[following] = ahead
                    queue.append((following, ahead))

        elapsed = 0
        for _ in range(runner_up[n]):
            if (elapsed // change) % 2 == 1:
                elapsed = (elapsed // change + 1) * change
            elapsed += time
        return elapsed
