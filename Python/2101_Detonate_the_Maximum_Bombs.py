# Author: Kaustav Ghosh
# https://leetcode.com/problems/detonate-the-maximum-bombs/

from collections import defaultdict, deque

class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    graph[i].append(j)

        best = 0
        for i in range(n):
            visited = set([i])
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            best = max(best, len(visited))
        return best
