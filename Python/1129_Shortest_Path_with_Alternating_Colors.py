# Author: Kaustav Ghosh
# 1129. Shortest Path with Alternating Colors
# https://leetcode.com/problems/shortest-path-with-alternating-colors/

from collections import deque

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        RED, BLUE = 0, 1
        graph = [[] for _ in range(n)]
        for u, v in redEdges:
            graph[u].append((v, RED))
        for u, v in blueEdges:
            graph[u].append((v, BLUE))

        result = [-1] * n
        result[0] = 0
        # (node, last_color)
        q = deque([(0, RED, 0), (0, BLUE, 0)])
        visited = {(0, RED), (0, BLUE)}
        while q:
            node, color, dist = q.popleft()
            for nb, edge_color in graph[node]:
                if edge_color != color and (nb, edge_color) not in visited:
                    visited.add((nb, edge_color))
                    if result[nb] == -1:
                        result[nb] = dist + 1
                    q.append((nb, edge_color, dist + 1))
        return result
