# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import defaultdict, deque

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set([source])
        q = deque([source])
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei == destination:
                    return True
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return False
