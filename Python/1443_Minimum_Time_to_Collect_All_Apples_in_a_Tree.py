# Author: Kaustav Ghosh
# Problem: Minimum Time to Collect All Apples in a Tree
# Approach: DFS sum of edge costs to subtrees containing apples

from collections import defaultdict

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)
            total = 0
            for child in graph[node]:
                if child not in visited:
                    child_cost = dfs(child)
                    if child_cost > 0 or hasApple[child]:
                        total += child_cost + 2
            return total

        return dfs(0)
