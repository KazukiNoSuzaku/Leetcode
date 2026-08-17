# Author: Kaustav Ghosh
# Problem: Second Minimum Time to Reach Destination
# Approach: All edges cost the same time, so the arrival time is a pure function of the number of edges (waiting at red signals depends only on elapsed time). BFS finds the smallest and second-smallest edge counts to reach n; simulate signal waiting for that second count

from collections import deque

class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        INF = float('inf')
        dist1 = [INF] * (n + 1)
        dist2 = [INF] * (n + 1)
        dist1[1] = 0
        dq = deque([(1, 0)])
        while dq:
            node, d = dq.popleft()
            for nb in graph[node]:
                nd = d + 1
                if nd < dist1[nb]:
                    dist2[nb] = dist1[nb]
                    dist1[nb] = nd
                    dq.append((nb, nd))
                elif dist1[nb] < nd < dist2[nb]:
                    dist2[nb] = nd
                    dq.append((nb, nd))

        steps = dist2[n]
        t = 0
        for _ in range(steps):
            if (t // change) % 2 == 1:      # red -> wait for green
                t = (t // change + 1) * change
            t += time
        return t
