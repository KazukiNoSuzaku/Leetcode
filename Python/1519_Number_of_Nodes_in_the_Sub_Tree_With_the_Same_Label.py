# Author: Kaustav Ghosh
# Problem: Number of Nodes in the Sub-Tree With the Same Label
# Approach: DFS returning label-frequency map per subtree; answer for each node = count of its own label in subtree

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

        ans = [0] * n

        def dfs(node, parent):
            counts = defaultdict(int)
            counts[labels[node]] += 1
            for child in graph[node]:
                if child != parent:
                    child_counts = dfs(child, node)
                    for k, v in child_counts.items():
                        counts[k] += v
            ans[node] = counts[labels[node]]
            return counts

        dfs(0, -1)
        return ans
