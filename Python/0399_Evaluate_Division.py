# You are given an array of variable pairs equations and an array of real numbers values,
# where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
# Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, return the answers.

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited = set()
            queue = deque([(src, 1.0)])
            while queue:
                node, prod = queue.popleft()
                if node == dst:
                    return prod
                visited.add(node)
                for nei, w in graph[node].items():
                    if nei not in visited:
                        queue.append((nei, prod * w))
            return -1.0

        return [bfs(s, d) for s, d in queries]
