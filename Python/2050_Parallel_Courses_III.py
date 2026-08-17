# Author: Kaustav Ghosh
# Problem: Parallel Courses III
# Approach: Since courses run in parallel, each finishes at its own duration plus the latest finish among its prerequisites. Process courses in topological order (Kahn) propagating finish times; the answer is the maximum finish time

from collections import deque

class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        for a, b in relations:
            graph[a].append(b)
            indeg[b] += 1

        finish = [0] * (n + 1)
        dq = deque()
        for course in range(1, n + 1):
            if indeg[course] == 0:
                finish[course] = time[course - 1]
                dq.append(course)

        while dq:
            u = dq.popleft()
            for v in graph[u]:
                finish[v] = max(finish[v], finish[u] + time[v - 1])
                indeg[v] -= 1
                if indeg[v] == 0:
                    dq.append(v)

        return max(finish)
