# Find all paths from node 0 to last node in a DAG.

# Author: Kaustav Ghosh

class Solution(object):
    def allPathsSourceTarget(self, graph):
        res = []
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path[:])
                return
            for nb in graph[node]:
                dfs(nb, path + [nb])
        dfs(0, [0])
        return res
