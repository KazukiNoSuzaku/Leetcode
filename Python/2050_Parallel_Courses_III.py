# Author: Kaustav Ghosh
# Problem 2050: Parallel Courses III

from collections import deque

class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        adj = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for prev, nxt in relations:
            adj[prev].append(nxt)
            indegree[nxt] += 1

        dist = [0] * (n + 1)
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)
                dist[i] = time[i - 1]

        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                dist[nei] = max(dist[nei], dist[node] + time[nei - 1])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return max(dist[1:n + 1])
