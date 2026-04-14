# Author: Kaustav Ghosh
# Premium Problem
class Solution(object):
    def checkContradictions(self, equations, values):
        # type: (List[List[str]], List[float]) -> bool
        graph = {}
        for (a, b), v in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, v))
            graph[b].append((a, 1.0 / v))

        val = {}
        eps = 1e-5

        def dfs(node, cur):
            val[node] = cur
            for nei, w in graph[node]:
                nxt = cur * w
                if nei in val:
                    if abs(val[nei] - nxt) > eps:
                        return True
                else:
                    if dfs(nei, nxt):
                        return True
            return False

        for node in graph:
            if node not in val:
                if dfs(node, 1.0):
                    return True
        return False
