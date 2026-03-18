# Author: Kaustav Ghosh
# Problem: 1519 - Number of Nodes in the Sub-Tree With the Same Label
# Approach: DFS counting label frequencies per subtree

from collections import defaultdict

class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        result = [0] * n

        def dfs(node, parent):
            counts = defaultdict(int)
            counts[labels[node]] = 1
            for child in graph[node]:
                if child != parent:
                    child_counts = dfs(child, node)
                    for c, cnt in child_counts.items():
                        counts[c] += cnt
            result[node] = counts[labels[node]]
            return counts

        dfs(0, -1)
        return result
