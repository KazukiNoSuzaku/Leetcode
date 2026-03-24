# Author: Kaustav Ghosh
# Problem 2045: Second Minimum Time to Reach Destination

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
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # BFS tracking up to 2 shortest distances per node
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0
        queue = deque([(1, 0)])  # (node, time_steps)
        while queue:
            node, d = queue.popleft()
            for nei in adj[node]:
                nd = d + 1
                if nd < dist[nei][0]:
                    dist[nei][0] = nd
                    queue.append((nei, nd))
                elif nd > dist[nei][0] and nd < dist[nei][1]:
                    dist[nei][1] = nd
                    queue.append((nei, nd))
        # Calculate actual time for second minimum path
        steps = dist[n][1]
        actual_time = 0
        for _ in range(steps):
            # Check if we need to wait for green light
            cycle = actual_time // change
            if cycle % 2 == 1:
                # Red light, wait until next green
                actual_time = (cycle + 1) * change
            actual_time += time
        return actual_time
